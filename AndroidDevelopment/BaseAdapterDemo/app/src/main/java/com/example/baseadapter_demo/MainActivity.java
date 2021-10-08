package com.example.baseadapter_demo;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.ListView;
import android.os.Bundle;


public class MainActivity extends AppCompatActivity  {

        ListView simpleList;
        String countryList[] = {"India", "China", "australia", "Spain", "America", "NewZealand"};
        int flags[] = {R.drawable.india, R.drawable.china, R.drawable.australia, R.drawable.spain, R.drawable.america, R.drawable.newzealand};

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            simpleList = (ListView) findViewById(R.id.simpleListView);
            CustomAdapter customAdapter = new CustomAdapter(getApplicationContext(), countryList, flags);
            simpleList.setAdapter(customAdapter);
        }}