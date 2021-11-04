package com.example.recyclerview_demo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.bumptech.glide.request.RequestOptions;

import java.util.ArrayList;

public class SecondActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        TextView textView = findViewById(R.id.second_textView);
        ImageView imageView = findViewById(R.id.second_imageView);

        ArrayList<String> animalImages = new ArrayList<>();
        animalImages.add("https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg");
        animalImages.add("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=1.00xw:0.756xh;0,0.0756xh&resize=980:*");
        animalImages.add("https://news.wttw.com/sites/default/files/styles/full/public/article/image-non-gallery/DSC_0993-Magic%20Dolphin.jpg?itok=VD7a_rue");
        animalImages.add("https://opimedia.azureedge.net/-/media/Images/MEN/Editorial/Blogs/Homesteading-and-Livestock/21-Things-to-Know-Before-Starting-a-Goat-Farm/goat-math-sq-jpg.jpg?la=en&hash=E8BD9D06BB68E87582DDEC28173ED44EF5368D57");
        animalImages.add("https://equusmagazine.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTc4NjI5NjMwMDkyMTI1OTg0/horse-galloping-on-sand.jpg");
        animalImages.add("https://www.offthegridnews.com/wp-content/uploads/2015/08/rooster-fameimagesDOTcom.jpg");
        animalImages.add("https://i.pinimg.com/564x/81/79/f1/8179f1c308aa6df254210e90d8958a1d.jpg");
        animalImages.add("https://worldanimalnews.com/wp-content/uploads/2020/05/beautiful-wolf.jpeg");

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            Integer value = (Integer) extras.get("key");
            String image_url= animalImages.get(value);

            Glide.with(this)
                    .load(image_url)
                    .apply(new RequestOptions().placeholder(R.drawable.loading))
                    .error(R.drawable.error_image)
                    .apply(new RequestOptions().override(400, 400))
                    .fitCenter() // scale to fit entire image within ImageView
                    .into(imageView);

            switch(value) {
                case 0:
                    textView.setText(R.string.cow_string);
                    break;
                case 1:
                    textView.setText(R.string.dog_string);
                    break;
                case 2:
                    textView.setText(R.string.dolphin_string);
                    break;
                case 3:
                    textView.setText(R.string.goat_string);
                    break;
                case 4:
                    textView.setText(R.string.horse_string);
                    break;
                case 5:
                    textView.setText(R.string.rooster_string);
                    break;
                case 6:
                    textView.setText(R.string.unicorn_string);
                    break;
                case 7:
                    textView.setText(R.string.wolf_string);
                    break;
                default:
                    textView.setText("nill");
                    break;
            }

        }

    }
}