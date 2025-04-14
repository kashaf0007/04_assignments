import streamlit as st

st.title("BMI Calculator ")
weight =  st.number_input("Enter your weight in kg :")
height = st.number_input("Enter your Height in cm :")
if st.button("Calculate BMI"):
 bmi = weight / ((height/100 )** 2 )
 st.write("Your BMI is :" , round(bmi , 2))
 if bmi < 18.5:
  st.write("You are underweight.")
 elif bmi <25 :
  st.write("You are normal weight.")
 elif bmi < 29:
  st.write("You are over weight.")
 else :
  st.write("You are obese.")