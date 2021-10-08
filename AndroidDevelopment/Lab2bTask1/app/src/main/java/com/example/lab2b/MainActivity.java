package com.example.lab2b;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
                Toast.makeText(getApplicationContext(), " onCreate() calls", Toast.LENGTH_LONG).show();

        Button send_btn = findViewById(R.id.send_1_to_2);
        send_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent send = new Intent(MainActivity.this, MainActivity2.class);
                startActivity(send);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(getApplicationContext(), " onStart() calls",
                Toast.LENGTH_LONG).show(); //onStart Called
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(getApplicationContext(), " First Activity onRestart() calls",
                Toast.LENGTH_LONG).show(); // The activity is between stopped and started.
    }

    @Override
    protected void onResume(){
        super.onResume();
        Toast.makeText(getApplicationContext(), " First Activity onResume() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity has become visible  // it is now "resumed"

    @Override
    protected void onPause(){
        super.onPause();
        Toast.makeText(getApplicationContext(), " First Activity onPause() calls",
                Toast.LENGTH_LONG).show();
    }   // this activity is about to be "paused"

    @Override
    protected void onStop(){
        super.onStop();
        Toast.makeText(getApplicationContext(), " First Activity onStop() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity is no longer visible    // it is now "stopped"

    @Override
    protected void onDestroy(){
        super.onDestroy();
        Toast.makeText(getApplicationContext(), " First Activity onDestroy() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity is about to be destroyed.
}