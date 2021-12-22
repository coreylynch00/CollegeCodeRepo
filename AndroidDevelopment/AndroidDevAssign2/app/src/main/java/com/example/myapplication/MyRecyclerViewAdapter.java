package com.example.myapplication;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MyRecyclerViewAdapter extends RecyclerView.Adapter<MyRecyclerViewAdapter.MyViewHolder> {

    private ArrayList<Weather> mList = new ArrayList<>();
    public MyRecyclerViewAdapter(ArrayList<Weather> mList){
        this.mList = mList;
    }

    @NonNull
    @Override
    public MyRecyclerViewAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.weather_row, parent, false);

        MyViewHolder myViewHolder = new MyViewHolder(view);

        return myViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull MyRecyclerViewAdapter.MyViewHolder holder, int position) {
        String city = "City: " + mList.get(position).getCity();
        holder.cityTextView.setText(city);

        String temp = "Temp: " + mList.get(position).getTemp();
        holder.tempTextView.setText(temp);

        String wind = "Wind: " + mList.get(position).getWind();
        holder.windTextView.setText(wind);
    }

    @Override
    public int getItemCount() {
        return mList.size();
    }
    @Override
    public int getItemViewType(int position) {
        return position;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    class MyViewHolder extends RecyclerView.ViewHolder {
        private TextView cityTextView;
        private TextView tempTextView;
        private TextView windTextView;

        public MyViewHolder(View view) {
            super(view);

            cityTextView = view.findViewById(R.id.textViewCity);
            tempTextView = view.findViewById(R.id.textViewTemp);
            windTextView = view.findViewById(R.id.textViewWind);
        }
    }

}
