package com.example.lab7proximitysensor;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.graphics.Color;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    TextView text;
    private SensorManager sensorManager;
    private Sensor proximitySensor;
    private final static int SENSOR_SENSITIVITY = 5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text = findViewById(R.id.textView);
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        proximitySensor = sensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);

    }

    @Override
    protected void onStart(){
        super.onStart();
        sensorManager.registerListener(this, proximitySensor, SensorManager.SENSOR_DELAY_NORMAL);
    }

    protected void onStop(){
        super.onStop();
        sensorManager.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {
        if (sensorEvent.sensor.getType() == Sensor.TYPE_PROXIMITY){
            if (sensorEvent.values[0] >= SENSOR_SENSITIVITY) {
                getWindow().getDecorView().setBackgroundColor(Color.GREEN);
                text.setText("Safe");
            }
            else if (sensorEvent.values[0] < 5 && sensorEvent.values[0] >= 2.5){
                getWindow().getDecorView().setBackgroundColor(Color.YELLOW);
                text.setText("Close");
            }
            else {
                getWindow().getDecorView().setBackgroundColor(Color.RED);
                text.setText("Dangerously Close");
            }
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int i) {

    }
}