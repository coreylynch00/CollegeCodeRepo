package com.example.json_test;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MyRecyclerViewAdapter extends RecyclerView.Adapter<MyRecyclerViewAdapter.MyViewHolder> {

    private ArrayList<Employee> mList = new ArrayList<>();
    public MyRecyclerViewAdapter(ArrayList<Employee> mList){
        this.mList = mList;
    }



    @NonNull
    @Override
    public MyRecyclerViewAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.employee_row, parent, false);
        MyViewHolder myViewHolder = new MyViewHolder(view);
        return myViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position)
    {
        String name = "Name: " + mList.get(position).getName();
        holder.nameTextView.setText(name);

        String gender = "Gender: " + mList.get(position).getGender();
        holder.genderTextView.setText(gender);

        String age = "Age: " + mList.get(position).getAge();
        holder.ageTextView.setText(age);
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

    class MyViewHolder extends RecyclerView.ViewHolder
    {
        private TextView nameTextView;
        private TextView genderTextView;
        private TextView ageTextView;

        public MyViewHolder(View view)
        {
            super(view);
            nameTextView = view.findViewById(R.id.textViewName);
            genderTextView = view.findViewById(R.id.textViewGender);
            ageTextView = view.findViewById(R.id.textViewAge);
        }
    }

}