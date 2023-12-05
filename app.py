# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:50:15 2023

@author: bhagy
"""

import pickle
import streamlit as st

load=open("model_random_forest.pkl","rb")
model=pickle.load(load)


def predict(Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business,Ease_of_Business,Energy_Usage,GDP,Health_Exp_percentage_GDP,Health_Exp_per_Capita,Hours_to_do_Tax,Infant_Mortality_Rate,Internal_Usage,Lending_Interest,Life_Expectancy_Female,Life_Expectancy_Male):
    prediction=model.predict([[Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business,Ease_of_Business,Energy_Usage,GDP,Health_Exp_percentage_GDP,Health_Exp_per_Capita,Hours_to_do_Tax,Infant_Mortality_Rate,Internal_Usage,Lending_Interest,Life_Expectancy_Female,Life_Expectancy_Male]])
    return prediction


def main():
    st.title("World Development Measurement")
    
    Birth_Rate=st.number_input("Birth Rate:")
    Business_Tax_Rate=st.number_input("Business Tax Rate:")
    CO2_Emissions=st.number_input("CO2 Emissions:")
    Days_to_Start_Business=st.number_input("Days to Start Business:")
    Ease_of_Business=st.number_input("Ease of Business:")
    Energy_Usage=st.number_input("Energy Usage:")
    GDP=st.number_input("GDP:")
    Health_Exp_percentage_GDP=st.number_input("Health Exp percentage GDP:")
    Health_Exp_per_Capita=st.number_input("Health Exp per Capita:")
    Hours_to_do_Tax=st.number_input("Hours to do Tax:")
    Infant_Mortality_Rate=st.number_input("Infant Mortality Rate:")
    Internal_Usage=st.number_input("Internal Usage:")
    Lending_Interest=st.number_input("Lending Interest:")
    Life_Expectancy_Female=st.number_input("Life_Expectancy_Female:")
    Life_Expectancy_Male=st.number_input("Life_Expectancy_Male:")
    
    
    
    if st.button("Predict"):
          result=predict(Birth_Rate,Business_Tax_Rate,CO2_Emissions,Days_to_Start_Business,Ease_of_Business,Energy_Usage,GDP,Health_Exp_percentage_GDP,Health_Exp_per_Capita,Hours_to_do_Tax,Infant_Mortality_Rate,Internal_Usage,Lending_Interest,Life_Expectancy_Female,Life_Expectancy_Male)
          if result ==0:
              st.success("Developing Country")
          elif result ==1:
              st.success("Developed Country")
          elif result ==2:
              st.success("Under Developed Country") 
          elif result ==3:
              st.success("Highly Developed Country")
          elif result==4:
              st.success(" Least Developed country")
                 


if __name__=="__main__":
    main()
              
          
    