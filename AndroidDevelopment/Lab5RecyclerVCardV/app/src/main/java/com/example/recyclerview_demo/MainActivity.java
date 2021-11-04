package com.example.recyclerview_demo;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements MyRecyclerViewAdapter.ItemClickListener {
    MyRecyclerViewAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // data to populate the RecyclerView with
        ArrayList<String> animalNames = new ArrayList<>();
        animalNames.add("Cow");
        animalNames.add("Dog");
        animalNames.add("Dolphin");
        animalNames.add("Goat");
        animalNames.add("Horse");
        animalNames.add("Rooster");
        animalNames.add("Unicorn");
        animalNames.add("Wolf");


        ArrayList<Integer> animalImages=new ArrayList<Integer>();

        animalImages.add(R.drawable.cow);
        animalImages.add(R.drawable.dog);
        animalImages.add(R.drawable.dolphin);
        animalImages.add(R.drawable.goat);
        animalImages.add(R.drawable.horse);
        animalImages.add(R.drawable.rooster);
        animalImages.add(R.drawable.unicorn);
        animalImages.add(R.drawable.wolf);

        // set up the RecyclerView
        //1- initialise the recyclerview
        RecyclerView recyclerView = findViewById(R.id.rvAnimals);
        //2-
        //recyclerView.setLayoutManager(new LinearLayoutManager(this));

        RecyclerView.LayoutManager manager = new GridLayoutManager(this, 2);
        recyclerView.setLayoutManager(manager);

        adapter = new MyRecyclerViewAdapter(this, animalNames,animalImages);
        adapter.setClickListener(this);
        recyclerView.setAdapter(adapter);
    }
    @Override
    public void onItemClick(View view, int position) {
        Toast.makeText(this, "You clicked " + adapter.getItem(position) + " on row number " + position, Toast.LENGTH_SHORT).show();

        Intent intent = new Intent(this, SecondActivity.class);
        intent.putExtra("key",(position));
        startActivity(intent);

    }



}