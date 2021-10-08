package com.example.lab3task2_passingvaluesintent;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class SecondActivity extends AppCompatActivity {

    // Defining Variable
    TextView text;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        // Initialize Variable
        text = (TextView)findViewById(R.id.textView);

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
           // The key argument here must match that used in the other activity
           String name = extras.getString("name");
           text.setText(name);
        }
    }
}