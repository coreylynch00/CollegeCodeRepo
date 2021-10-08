package com.example.lab3task1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    RadioButton jazz, pop, classic;
    Button play;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        jazz = (RadioButton)findViewById(R.id.rdbJazz);
        pop = (RadioButton)findViewById(R.id.rdbPop);
        classic = (RadioButton)findViewById(R.id.rdbClassic);
        Button btn = (Button)findViewById(R.id.getBtn);

        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                String result = "Selected Genre: ";
                result+=
                        (jazz.isChecked())?"Jazz":(pop.isChecked())?"Pop":(classic.isChecked())?"Classic":"";
                Toast.makeText(getApplicationContext(), result, Toast.LENGTH_SHORT).show();
            }
        });
    }
}