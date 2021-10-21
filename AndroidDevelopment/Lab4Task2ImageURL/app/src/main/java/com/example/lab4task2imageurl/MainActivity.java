package com.example.lab4task2imageurl;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    ImageView rossi, marquez, lorenzo, pedrosa, vinales;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        rossi = (ImageView) findViewById(R.id.imageViewRossi);
        marquez = (ImageView) findViewById(R.id.imageViewMarquez);
        lorenzo = (ImageView) findViewById(R.id.imageViewLorenzo);
        pedrosa = (ImageView) findViewById(R.id.imageViewPedrosa);
        vinales = (ImageView) findViewById(R.id.imageViewVinales);
    }

    public void openRossi(View view) {
        String urlRossi = "https://en.wikipedia.org/wiki/Valentino_Rossi";

        Uri webpage = Uri.parse(urlRossi);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void openMarquez(View view) {
        String urlMarquez = "https://en.wikipedia.org/wiki/Marc_Márquez";

        Uri webpage = Uri.parse(urlMarquez);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void openLorenzo(View view) {
        String urlLorenzo = "https://en.wikipedia.org/wiki/Jorge_Lorenzo";

        Uri webpage = Uri.parse(urlLorenzo);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void openPedrosa(View view) {
        String urlPedrosa = "https://en.wikipedia.org/wiki/Dani_Pedrosa";

        Uri webpage = Uri.parse(urlPedrosa);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }

    public void openVinales(View view) {
        String urlVinales = "https://en.wikipedia.org/wiki/Maverick_Viñales";

        Uri webpage = Uri.parse(urlVinales);
        Intent intent = new Intent(Intent.ACTION_VIEW, webpage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
        else {
            Log.d("ImplicitIntents", "Cant handle this intent!");
        }
    }
}