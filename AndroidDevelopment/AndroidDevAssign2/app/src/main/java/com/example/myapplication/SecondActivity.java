package com.example.myapplication;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Build;
import android.os.Bundle;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

public class SecondActivity extends AppCompatActivity {

    private ArrayList<Weather> weatherList = new ArrayList<>();
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        getWeatherList();
        setUIRef();
    }
    private void setUIRef()
    {
        RecyclerView recyclerView = findViewById(R.id.RV);
        MyRecyclerViewAdapter myRecyclerViewAdapter = new MyRecyclerViewAdapter(weatherList);
        recyclerView.setAdapter(myRecyclerViewAdapter);
        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(SecondActivity.this, RecyclerView.VERTICAL, false);
        recyclerView.setLayoutManager(linearLayoutManager);
    }
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    private void getWeatherList()
    {
        String myJSONStr = loadJSONFromAsset("weather.json");
        try
        {

            JSONObject rootJSONObject = new JSONObject(myJSONStr);

            JSONArray weatherJSONArray = rootJSONObject.getJSONArray("weather");
            for (int i = 0; i < weatherJSONArray.length(); i++)
            {

                Weather mweather = new Weather();

                JSONObject jsonObject = weatherJSONArray.getJSONObject(i);

                mweather.setCity(jsonObject.getString("City"));
                mweather.setTemp(jsonObject.getString("Temp"));
                mweather.setWind(jsonObject.getString("Wind"));

                weatherList.add(mweather);
            }

        } catch (JSONException e)
        {
            e.printStackTrace();
        }
    }
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public String loadJSONFromAsset(String fileName)
    {
        String json;
        try
        {
            InputStream is = getAssets().open(fileName);
            int size = is.available();
            byte[] buffer = new byte[size];
            //noinspection ResultOfMethodCallIgnored
            is.read(buffer);
            is.close();
            json = new String(buffer, StandardCharsets.UTF_8);
        } catch (IOException ex)
        {
            ex.printStackTrace();
            return null;
        }
        return json;
    }
}