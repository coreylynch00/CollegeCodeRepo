package com.example.gson_tutorial;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.res.AssetManager;
import android.os.Bundle;

import com.google.gson.Gson;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;

public class MainActivity extends AppCompatActivity {
    private CountryData mCountryData;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getCountryList();
        setUIRef();

    }



    private void getCountryList()
    {
        AssetManager assetManager = getAssets();
        try
        {
            //create a Gson object
            Gson gson = new Gson();

            // define the input stream
            InputStream inputStream = assetManager.open("data.json");

            //create a reader
            Reader reader = new InputStreamReader(inputStream);

            // from reader create an employee object
            mCountryData = gson.fromJson(reader, CountryData.class);

        } catch (IOException e)
        {
            e.printStackTrace();
        }
    }
    private void setUIRef()
    {
        RecyclerView recyclerView = findViewById(R.id.RV);

        MyRecyclerviewAdapter myRecyclerViewAdapter = new MyRecyclerviewAdapter(mCountryData.getCountries());

        recyclerView.setAdapter(myRecyclerViewAdapter);

        LinearLayoutManager linearLayoutManager;

        linearLayoutManager= new LinearLayoutManager(MainActivity.this, RecyclerView.VERTICAL, false);

        recyclerView.setLayoutManager(linearLayoutManager);

    }

}