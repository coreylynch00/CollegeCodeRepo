package com.example.demo_json;

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

public class MainActivity extends AppCompatActivity {

    private ArrayList<Employee> mEmployeesList = new ArrayList<>();
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getEmployeeList();
        setUIRef();
    }
    private void setUIRef()
    {
        RecyclerView recyclerView = findViewById(R.id.rv);
        MyRecyclerViewAdapter myRecyclerViewAdapter = new MyRecyclerViewAdapter(mEmployeesList);
        recyclerView.setAdapter(myRecyclerViewAdapter);
        LinearLayoutManager linearLayoutManager = new LinearLayoutManager(MainActivity.this, RecyclerView.VERTICAL, false);
        recyclerView.setLayoutManager(linearLayoutManager);
    }
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    private void getEmployeeList()
    {
        String myJSONStr = loadJSONFromAsset("employee_data.json");
        try
        {
            //Get root JSON object node
            JSONObject rootJSONObject = new JSONObject(myJSONStr);
            //Get employee array node
            JSONArray employeeJSONArray = rootJSONObject.getJSONArray("employee");
            for (int i = 0; i < employeeJSONArray.length(); i++)
            {
                //Create a temp object of the employee model class
                Employee aEmployee = new Employee();

                //Get employee JSON object node
                JSONObject jsonObject = employeeJSONArray.getJSONObject(i);

                //Get employee details
                aEmployee.setName(jsonObject.getString("name"));
                aEmployee.setGender(jsonObject.getString("gender"));
                aEmployee.setAge(jsonObject.getInt("age"));

                //Add employee object to the list
                mEmployeesList.add(aEmployee);
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