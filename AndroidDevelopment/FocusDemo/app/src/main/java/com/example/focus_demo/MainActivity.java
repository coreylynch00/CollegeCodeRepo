package com.example.focus_demo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
       // setContentView(R.layout.activity_main); // use for default focus
        // setContentView(R.layout.new_focus); // use for directed focus
        setContentView(R.layout.scroll_example_layout);
    }
}