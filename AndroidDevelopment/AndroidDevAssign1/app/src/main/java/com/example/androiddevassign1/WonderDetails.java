package com.example.androiddevassign1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;
import java.util.ArrayList;

public class WonderDetails extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_wonder_details);

        //Define & initialize variables
        TextView wonderTextView = findViewById(R.id.wonderDetailsTextView);
        ImageView wonderImageView = findViewById(R.id.wonderDetailsImageView);
        Button locationButton = findViewById(R.id.locationButton);
        TextView linkTextView = findViewById(R.id.textViewLink);
        TextView heading = findViewById(R.id.textViewHeading);

        //Create array with Glide images
        ArrayList<String> wonderImages = new ArrayList<>();
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/e/e3/Kheops-Pyramid.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/6/6f/The_Great_Wall_of_China_at_Jinshanling.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/b/b7/The_Monastery%2C_Petra%2C_Jordan8.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/f/f7/KOLOSSEUM_-_panoramio.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/7/7a/Chichen-Itza-Castillo-Seen-From-East.JPG");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/e/eb/Machu_Picchu%2C_Peru.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/c/c8/Taj_Mahal_in_March_2004.jpg");
        wonderImages.add("https://upload.wikimedia.org/wikipedia/commons/3/3a/Unique_Moment_with_the_Moon_and_Christ_the_Redeemer_3.jpg");

        Bundle extras = getIntent().getExtras();
        if (extras != null){
            Integer val = (Integer) extras.get("key");
            String image_url = wonderImages.get(val);

            Glide.with(this)
                    .load(image_url)
                    .apply(new RequestOptions().placeholder(R.drawable.loading))
                    .error(R.drawable.error_image)
                    .apply(new RequestOptions().override(400, 400))
                    .fitCenter()
                    .into(wonderImageView);

            //Switch statement for users card option
            switch(val) {

                case 0:
                    heading.setText("Pyramid Of Giza");
                    wonderTextView.setText(R.string.pyramid_string);
                    //OnClickListener for location button
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "pyramid of giza, Al Haram, Nazlet El-Semman, Al Giza Desert, Egypt";
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
                    });
                    //OnClickListener for link to YouTube video
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=GtJW-8ZvNE8";
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
                    });
                    break;

                case 1:
                    heading.setText("Great Wall Of China");
                    wonderTextView.setText(R.string.greatwall_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Great Wall of China, Mutianyu Great Wall, Huairou District, Beijing, China";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=pZGgHmqySa8";
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
                    });
                    break;

                case 2:
                    heading.setText("Petra");
                    wonderTextView.setText(R.string.petra_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Petra, Wadi Musa, Jordan";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=pOZRoZI76nA";
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
                    });
                    break;

                case 3:
                    heading.setText("Colosseum");
                    wonderTextView.setText(R.string.colosseum_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Colosseum, Piazza del Colosseo, Rome, Metropolitan City of Rome, Italy";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=U6oPfmJcU8s";
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
                    });
                    break;

                case 4:
                    heading.setText("Chichén Itzá");
                    wonderTextView.setText(R.string.chichen_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Chichén-Itzá, Yucatan, Mexico";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=RanNSvO4AcQ";
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
                    });
                    break;

                case 5:
                    heading.setText("Machu Picchu");
                    wonderTextView.setText(R.string.machu_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Machu Picchu, Peru";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=5cVSWA37xiI";
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
                    });
                    break;

                case 6:
                    heading.setText("Taj Mahal");
                    wonderTextView.setText(R.string.taj_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Taj Mahal, Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh, India";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=I6i8cLXPGQE";
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
                    });
                    break;

                case 7:
                    heading.setText("Christ The Redeemer");
                    wonderTextView.setText(R.string.christ_string);
                    locationButton.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            String loc = "Christ the Redeemer - Alto da Boa Vista, Rio de Janeiro - State of Rio de Janeiro, Brazil";
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
                    });
                    linkTextView.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View view) {
                            //Define URL
                            String url = "https://www.youtube.com/watch?v=6Hvv0rHukWo";
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
                    });
                    break;
            }
        }
    }
}