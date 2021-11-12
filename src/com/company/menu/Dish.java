package com.company.menu;

import java.util.ArrayList;
import java.util.List;

public class Dish extends MenuItem{
    String description;
    ArrayList<String> allergens;
    public Dish(String name, double price, String description, int id, ArrayList<String> allergens){
        super.name = name;
        super.price = price;
        this.description = description;
        this.allergens = allergens;
    }
    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString(){
        StringBuilder allergenList = new StringBuilder();
        for(String item : allergens) {
            allergens.add(item.toString() + "\n");
        }
        return super.toString() + "Description " + description +
                                  "Allergens " + allergenList;
    }
}
