package com.example.gson_tutorial;

import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class CountryData {
        @SerializedName("country")
        private ArrayList<Country> countries = new ArrayList<>();

        public ArrayList<Country> getCountries()
        {
            return countries;
        }

        public void setCountries(ArrayList<Country> countries)
        {
            this.countries = countries;
        }

    }
