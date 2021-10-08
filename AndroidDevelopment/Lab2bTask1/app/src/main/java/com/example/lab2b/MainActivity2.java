package com.example.lab2b;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.os.Bundle;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        Button send_btn = findViewById(R.id.send_2_to_1);
        send_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent send = new Intent(MainActivity2.this, MainActivity.class);
                startActivity(send);
            }
        });
    }
    @Override
    protected void onStart() {
        super.onStart();
        Toast.makeText(getApplicationContext(), "Second Activity onStart() calls",
                Toast.LENGTH_LONG).show(); //onStart Called
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Toast.makeText(getApplicationContext(), "Second Activity onRestart() calls",
                Toast.LENGTH_LONG).show(); // The activity is between stopped and started.
    }

    @Override
    protected void onResume(){
        super.onResume();
        Toast.makeText(getApplicationContext(), "Second Activity onResume() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity has become visible  // it is now "resumed"

    @Override
    protected void onPause(){
        super.onPause();
        Toast.makeText(getApplicationContext(), "Second Activity onPause() calls",
                Toast.LENGTH_LONG).show();
    }   // this activity is about to be "paused"

    @Override
    protected void onStop(){
        super.onStop();
        Toast.makeText(getApplicationContext(), "Second Activity onStop() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity is no longer visible    // it is now "stopped"

    @Override
    protected void onDestroy(){
        super.onDestroy();
        Toast.makeText(getApplicationContext(), "Second Activity onDestroy() calls",
                Toast.LENGTH_LONG).show();
    }   // The activity is about to be destroyed.
}