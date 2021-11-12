package com.example.test_broadcast;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

public class MyReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        String intentAction = intent.getAction();
        if (intentAction == Intent.ACTION_BATTERY_LOW){
            Toast.makeText(context, "Battery Low", Toast.LENGTH_LONG).show();
        }
    }
}

