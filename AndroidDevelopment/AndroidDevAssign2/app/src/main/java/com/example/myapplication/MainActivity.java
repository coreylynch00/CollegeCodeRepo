package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    EditText location;
    Button search, clear, save;
    TextView countryName, tvWind, tvMin, tvMax, tvFeel, tvDescription, tvDetails, tvMainTemp, tvDatabase;
    ImageView icon;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        location = findViewById(R.id.editTextLocation);
        search = findViewById(R.id.buttonSearch);
        countryName = findViewById(R.id.textViewCountry);
        tvWind = findViewById(R.id.textViewWind);
        tvMin = findViewById(R.id.textViewMin);
        tvMax = findViewById(R.id.textViewMax);
        tvFeel = findViewById(R.id.textViewFeel);
        tvDescription = findViewById(R.id.textViewDescription);
        tvDetails = findViewById(R.id.textViewDetails);
        tvMainTemp = findViewById(R.id.textViewMainTemp);
        icon = findViewById(R.id.imageViewIcon);
        clear = findViewById(R.id.buttonClear);
        save = findViewById(R.id.buttonSave);
        tvDatabase = findViewById(R.id.textViewDatabase);

        search.setOnClickListener(this);
        clear.setOnClickListener(this);
        save.setOnClickListener(this);
        tvDatabase.setOnClickListener(this);
    }

    @SuppressLint("NonConstantResourceId")
    @Override
    public void onClick(View view) {
        switch(view.getId()){
            case R.id.buttonSearch:
                clear.setVisibility(View.VISIBLE);
                save.setVisibility(View.VISIBLE);
                tvDetails.setVisibility(View.VISIBLE);
                tvDatabase.setVisibility(View.VISIBLE);
                getWeather();
                break;
            case R.id.buttonClear:
                startActivity(new Intent(MainActivity.this, MainActivity.class));
                Toast.makeText(MainActivity.this, "Page Reset!", Toast.LENGTH_LONG).show();
                break;
            case R.id.buttonSave:
                saveWeather();
                break;
            case R.id.textViewDatabase:
                startActivity(new Intent(MainActivity.this, SecondActivity.class));
                break;
        }
    }

    private void getWeather() {
        final String city = location.getText().toString();
        if(TextUtils.isEmpty(city)){
            location.setError("You must input a city!");
            location.requestFocus();
            return;
        }

        // Used this API instead of MetaWeather. Data would not display with MetaWeather on my laptop, but worked on my PC.
        // Not sure what the issue was but OpenWeather appears to be more reliable on my system.
        String url ="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=462f445106adc1d21494341838c10019&units=metric";
        StringRequest stringRequest = new StringRequest(Request.Method.GET,url,
                new Response.Listener<String>() {
                    @SuppressLint({"SetTextI18n", "UseCompatLoadingForDrawables"})
                    @Override
                    public void onResponse(String response) {

                        try {
                            //Create JSON object
                            JSONObject jsonObject = new JSONObject(response);

                            // Set Icon and Find Weather Description
                            // https://openweathermap.org/weather-conditions
                            JSONArray jsonArray = jsonObject.getJSONArray("weather");
                            JSONObject obj = jsonArray.getJSONObject(0);
                            String description = obj.getString("main");
                            tvDescription.setText(description);

                            switch (description) {
                                case "Clouds":
                                    icon.setBackground(getResources().getDrawable(R.drawable.cloud));
                                    break;
                                case "Thunderstorm":
                                    icon.setBackground(getResources().getDrawable(R.drawable.thunderstorm));
                                    break;
                                case "Drizzle":
                                    icon.setBackground(getResources().getDrawable(R.drawable.drizzle));
                                    break;
                                case "Rain":
                                    icon.setBackground(getResources().getDrawable(R.drawable.rain));
                                    break;
                                case "Snow":
                                    icon.setBackground(getResources().getDrawable(R.drawable.snow));
                                    break;
                                case "Clear":
                                    icon.setBackground(getResources().getDrawable(R.drawable.clear));
                                    break;
                                default:
                                    icon.setBackground(getResources().getDrawable(R.drawable.fog));
                                    break;
                            }

                            // Find Date/Time
                            Calendar calendar = Calendar.getInstance();
                            @SuppressLint("SimpleDateFormat") SimpleDateFormat sd = new SimpleDateFormat("HH:mm   |  E, dd MMM yyyy");
                            String date = sd.format(calendar.getTime());

                            // Find Country
                            JSONObject objectCountry = jsonObject.getJSONObject("sys");
                            String country = objectCountry.getString("country");
                            countryName.setText(city+", "+country +"   |  "+date);

                            // Find Temp
                            JSONObject objectTemp = jsonObject.getJSONObject("main");
                            double temp = objectTemp.getDouble("temp");
                            tvMainTemp.setText(temp+" °C");

                            // Find Min Temp
                            JSONObject objectMin = jsonObject.getJSONObject("main");
                            double mintemp = objectMin.getDouble("temp_min");
                            tvMin.setText("Min Temp: "+mintemp+" °C");

                            // Find Max Temp
                            JSONObject objectMax = jsonObject.getJSONObject("main");
                            double maxtemp = objectMax.getDouble("temp_max");
                            tvMax.setText("Max Temp: "+maxtemp+" °C");

                            // Find Feels Like Temp
                            JSONObject objectFeel = jsonObject.getJSONObject("main");
                            double feels_find = objectFeel.getDouble("feels_like");
                            tvFeel.setText("Feels Like: "+feels_find+" °C");

                            // Find Wind Speed
                            //find wind speed
                            JSONObject object9 = jsonObject.getJSONObject("wind");
                            String wind_find = object9.getString("speed");
                            tvWind.setText("Wind Speed: "+wind_find+" KM/H");

                        }
                        catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(MainActivity.this,error.getLocalizedMessage(),Toast.LENGTH_SHORT).show();
            }
        });

        RequestQueue requestQueue = Volley.newRequestQueue(MainActivity.this);
        requestQueue.add(stringRequest);
    }

    private void saveWeather() { //throws JSONException, IOException
        startActivity(new Intent(MainActivity.this, MainActivity.class));
        Toast.makeText(MainActivity.this, "Data Saved!", Toast.LENGTH_LONG).show();

        /**
         *
         * I COULDN'T FIGURE OUT WHY I WAS GETTING THIS ERROR
         * THIS IS MY ATTEMPT AT SAVING THE DATA TO A JSON FILE WHERE
         * IT WOULD THEN BE DISPLAYED TO RECYCLERVIEW IN SECOND ACTIVITY
         *
        String sCity = location.getText().toString();
        String sTemp = tvMainTemp.getText().toString();
        String sWind = tvWind.getText().toString();

        JSONObject jsonObject = new JSONObject();
        jsonObject.put("City", sCity);
        jsonObject.put("Temp", sTemp);
        jsonObject.put("Wind", sWind);
        return jsonObject;

        String weatherStr = jsonObject.toString();
        Context context = this;
        File file = new File(context.getFilesDir(), "weather.json");
        FileWriter fileWriter = new FileWriter(file);
        BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
        bufferedWriter.write(weatherStr);
        bufferedWriter.close();
        **/
    }
}