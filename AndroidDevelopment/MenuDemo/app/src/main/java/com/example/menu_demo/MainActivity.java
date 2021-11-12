package com.example.menu_demo;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.PopupMenu;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
 Button btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView pressView = (TextView)findViewById(R.id.tv);
        //register if for context
        registerForContextMenu(pressView);
        btn = findViewById(R.id.button_s);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                PopupMenu popup= new PopupMenu(MainActivity.this, v);
                popup.setOnMenuItemClickListener(MainActivity.this::onMenuItemClick);
                popup.inflate(R.menu.popup_menu);
                popup.show();
            }
        });

    }


    public boolean onMenuItemClick(MenuItem item){
        Toast.makeText(this,"Selected Item " + item.getTitle(),Toast.LENGTH_LONG).show();
    switch(item.getItemId()){
        case R.id.first_item:
            return true;
        case R.id.second_item:
            return true;
        default:
            return false;
    }

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.options_menu, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        Toast.makeText(this, "Selected Item: " + item.getTitle(), Toast.LENGTH_SHORT).show();
        switch (item.getItemId()) {
            case R.id.option_Yellow:
                // do your code
                getWindow().getDecorView().setBackgroundColor(Color.YELLOW);
                return true;
            case R.id.option_Red:
                getWindow().getDecorView().setBackgroundColor(Color.RED);
                return true;
            case R.id.option_Blue:
                // do your code
                getWindow().getDecorView().setBackgroundColor(Color.BLUE);
                return true;
            case R.id.option_Green:
                // do your code
                getWindow().getDecorView().setBackgroundColor(Color.GREEN);
                return true;
            case R.id.option_White:
                // do your code
                getWindow().getDecorView().setBackgroundColor(Color.WHITE);
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }


    @Override
    public void onCreateContextMenu(ContextMenu menuItem, View v, ContextMenu.ContextMenuInfo menuInfo) {
        super.onCreateContextMenu(menuItem, v, menuInfo);
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.context_menu, menuItem);
    }
    @Override
    public boolean onContextItemSelected(MenuItem item) {
        Toast.makeText(this, "Selected Item: " + item.getTitle(), Toast.LENGTH_SHORT).show();
        switch (item.getItemId()) {
            case R.id.option1:
                // do your code
                return true;
            case R.id.option2:
                // do your code
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }


    }

}