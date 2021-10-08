package com.example.list_demo;

import androidx.appcompat.app.AppCompatActivity;
import android.widget.ListView;
import android.os.Bundle;
import android.widget.ArrayAdapter;

public class MainActivity extends AppCompatActivity {

    // Array of strings...
    ListView simpleList;
    String countryList[] = {"India", "China", "Australia", "Spain", "America", "NewZealand"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        simpleList = (ListView)findViewById(R.id.simpleListView);
        ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this, R.layout.activity_list_view, R.id.textView, countryList);
        simpleList.setAdapter(arrayAdapter);
    }

}