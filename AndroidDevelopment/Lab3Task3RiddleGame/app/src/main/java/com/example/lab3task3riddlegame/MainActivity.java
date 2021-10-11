package com.example.lab3task3riddlegame;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // Define variables
    EditText editname;
    TextView text;
    RadioButton easy, medium, hard;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editname = (EditText) findViewById(R.id.editName);
        text = (TextView) findViewById(R.id.textView);
        easy = (RadioButton) findViewById(R.id.radioEasy);
        medium = (RadioButton) findViewById(R.id.radioMedium);
        hard = (RadioButton) findViewById(R.id.radioHard);
        btn = (Button) findViewById(R.id.button);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                // Determine which radio button is checked
                String result = "";
                result += (easy.isChecked())?"EASY":(medium.isChecked())?"MEDIUM":(hard.isChecked())?"HARD":"";
                // Convert name to a string type
                String name = editname.getText().toString();

                // Create intent
                Intent send = new Intent(MainActivity.this, SecondActivity.class);

                send.putExtra("name", name);
                send.putExtra("level", result);

                startActivity(send);
            }
        });

    }
}