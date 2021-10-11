package com.example.lab3task3riddlegame;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.w3c.dom.Text;

public class SecondActivity extends AppCompatActivity {

    TextView textName, textQuestion, textAnswer;
    Button showAns;
    String answerStr;
    String questionStr;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        // Initialize
        textName = (TextView) findViewById(R.id.textViewName);
        textQuestion = (TextView) findViewById(R.id.textViewQuestion);
        textAnswer = (TextView) findViewById(R.id.textViewAnswer);
        showAns = (Button) findViewById(R.id.buttonAnswer);


        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            String name = extras.getString("name");
            String level = extras.getString("level");
            textName.setText("Hello " + name + ",");

                switch(level) {
                    case "EASY":
                        questionStr = getString(R.string.riddle_easy);
                        answerStr = getString(R.string.ans_easy);
                        break;
                    case "MEDIUM":
                        questionStr = getString(R.string.riddle_medium);
                        answerStr = getString(R.string.ans_medium);
                        break;
                    case "HARD":
                        questionStr = getString(R.string.riddle_hard);
                        answerStr = getString(R.string.ans_hard);
                        break;

            }

            textQuestion.setText(questionStr);
        }

        showAns.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                textAnswer.setText(answerStr);
            }
        });
    }
}