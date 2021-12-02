package com.example.gson_tutorial;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MyRecyclerviewAdapter extends RecyclerView.Adapter<MyRecyclerviewAdapter.MyViewHolder> {
    private ArrayList<Country> mList = new ArrayList<>();
    public MyRecyclerviewAdapter(ArrayList<Country> mList){
        this.mList = mList;
    }

    @NonNull
    @Override
    public MyRecyclerviewAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.data_row, parent, false);
        MyViewHolder myViewHolder = new MyViewHolder(view);
        return myViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull MyRecyclerviewAdapter.MyViewHolder holder, int position) {
        String name = "Name: " + mList.get(position).getName();
        holder.nameTV.setText(name);

        String gender = "Language: " + mList.get(position).getLanguage();
        holder.languageTV.setText(gender);
    }

    @Override
    public int getItemCount() {
        return mList.size();
    }
    @Override
    public int getItemViewType(int position)
    {
        return position;
    }

    @Override
    public long getItemId(int position)
    {
        return position;
    }

    public class MyViewHolder extends RecyclerView.ViewHolder
    {
        private TextView nameTV;
        private TextView languageTV;
        public MyViewHolder(View view)
        {
            super(view);
            nameTV = view.findViewById(R.id.nameTV);
            languageTV = view.findViewById(R.id.languageTV);

        }
    }
}
