package com.example.lab3task1implicitintent;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ShareCompat;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    EditText textWebsite, textLocation, textShare;
    Button openWebsite, openLocation, openShare;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textWebsite = (EditText) findViewById(R.id.editTextWebsite);
        textLocation = (EditText) findViewById(R.id.editTextLocation);
        textShare = (EditText) findViewById(R.id.editTextShare);
        openWebsite = (Button) findViewById(R.id.openWebsite);
        openLocation = (Button) findViewById(R.id.openLocation);
        openShare = (Button) findViewById(R.id.openShare);
    }

    public void openWebsite(View view) {
        //Get URL text
        String url = textWebsite.getText().toString();

        //Parse the URI to create intent
        Uri webpage = Uri.parse(url);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        //Find an activity to handle the intent and start that activity
        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void openLocation(View view) {
        //Get string indicating location
        String loc = textLocation.getText().toString();

        //Parse location and create intent
        Uri addressUri = Uri.parse("geo:0,0?q=" + loc);
        Intent intent = new Intent(Intent.ACTION_VIEW, addressUri);

        //Find an activity to handle the intent and start that activity
        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void shareText(View view) {
        String txt = textShare.getText().toString();
        String mimeType = "text/plain";
        ShareCompat.IntentBuilder
                .from(this)
                .setText(mimeType)
                .setChooserTitle("Choose Application")
                .setText(txt)
                .startChooser();
    }
}