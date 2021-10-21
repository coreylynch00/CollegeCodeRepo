package com.example.demo_fragments;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
    Button firstFragmentBtn,secondFragmentBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firstFragmentBtn=findViewById(R.id.button1);
        secondFragmentBtn=findViewById(R.id.button2);

        firstFragmentBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
             replaceFragment(new fragment1());
            }
        });

        secondFragmentBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
             replaceFragment(new fragment2());
            }
        });
    }

    private void replaceFragment(Fragment fragment) {
        //1- create an instance of  fragment manager
        FragmentManager fragmentManager = getSupportFragmentManager();
        //2- create and start the fragment transaction
        FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
        //3- connect the fragment transaction to frame layout passing new fragment to be placed
        fragmentTransaction.replace(R.id.frameLayout,fragment);
        //4- Commit the transaction
        fragmentTransaction.commit();
    }
}