package com.example.lab3task2_passingvaluesintent;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    // Defining Variables
    EditText editname;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initializing Variables
        editname = (EditText)findViewById(R.id.editName);
        btn = (Button)findViewById(R.id.button);

        // Creating onClick method
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = editname.getText().toString();
                // Creating Intent
                Intent send = new Intent(MainActivity.this, SecondActivity.class);
                // Send the user input to SecondActivity
                send.putExtra("name", name);
                startActivity(send);
            }
        });
    }
}