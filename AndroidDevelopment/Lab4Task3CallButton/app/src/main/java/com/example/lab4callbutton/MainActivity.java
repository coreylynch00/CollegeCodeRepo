package com.example.lab4callbutton;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText phoneNumber;
    Button call;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phoneNumber = (EditText) findViewById(R.id.editTextPhoneNumber);
        call = (Button) findViewById(R.id.buttonCall);
        call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Get String
                String num = phoneNumber.getText().toString().trim();
                //Parse String
                Uri uri = Uri.parse(num);
                //Create Intent
                Intent intent = new Intent(Intent.ACTION_DIAL, uri);
                //Set intent data
                intent.setData(Uri.parse("tel:" + num));
                //Start Activity
                startActivity(intent);
            }
        });
    }
}