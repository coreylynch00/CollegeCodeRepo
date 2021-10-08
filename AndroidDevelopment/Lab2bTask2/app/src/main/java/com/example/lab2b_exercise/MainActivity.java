package com.example.lab2b_exercise;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Code to send first button to ELon page
        Button buttonFirst = findViewById(R.id.button1);
        buttonFirst.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent send = new Intent(MainActivity.this, ElonActivity.class);
                startActivity(send);
            }
        });

        // Code to send second button to Rossi page
        Button buttonSecond = findViewById(R.id.button2);
        buttonSecond.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent send = new Intent(MainActivity.this, RossiActivity.class);
                startActivity(send);
            }
        });

        // Code to send third button to Gates page
        Button buttonThird = findViewById(R.id.button3);
        buttonThird.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent send = new Intent(MainActivity.this, GatesActivity.class);
                startActivity(send);
            }
        });
    }
}