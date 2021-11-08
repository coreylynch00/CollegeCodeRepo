package com.example.androiddevassign1;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements MyRecyclerViewAdapter.ItemClickListener{

    //Declare RecyclerView
    MyRecyclerViewAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Create array for the 8 wonders
        ArrayList<String> wonders = new ArrayList<>();
        //Populate the array with data - each wonder
        wonders.add("Pyramid of Giza");
        wonders.add("Great Wall of China");
        wonders.add("Petra");
        wonders.add("Colosseum");
        wonders.add("Chichen Itza");
        wonders.add("Machu Picchu");
        wonders.add("Taj Mahal");
        wonders.add("Christ the Redeemer");

        //Create array to store images of wonders
        ArrayList<Integer> wonderImages = new ArrayList<>();
        wonderImages.add(R.drawable.pyramid);
        wonderImages.add(R.drawable.greatwall);
        wonderImages.add(R.drawable.petra);
        wonderImages.add(R.drawable.colosseum);
        wonderImages.add(R.drawable.chichen);
        wonderImages.add(R.drawable.machu);
        wonderImages.add(R.drawable.taj);
        wonderImages.add(R.drawable.christ);

        //Create RecyclerView
        RecyclerView rv = findViewById(R.id.rvWonders);
        //Initialize LayoutManager
        RecyclerView.LayoutManager manager = new GridLayoutManager(this, 1);
        //Set LayoutManager for RecyclerView
        rv.setLayoutManager(manager);
        //Initialize RecyclerView
        adapter = new MyRecyclerViewAdapter(this, wonders, wonderImages);
        adapter.setClickListener(this);
        rv.setAdapter(adapter);

    }

    @Override
    //Method to pass user to the fragment of their choice & display toast message of choice
    public void onItemClick(View view, int position){
        Toast.makeText(this, "Let's teach you about the " + adapter.getItem(position) + "!", Toast.LENGTH_SHORT).show();
        //Create intent, pass user from MainActivity to WonderDetails fragment
        Intent intent = new Intent(this, WonderDetails.class);
        intent.putExtra("key", (position));
        startActivity(intent);
    }
}