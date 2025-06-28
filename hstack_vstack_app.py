
import streamlit as st
import numpy as np

st.title("NumPy Array Stacker")

input_a = st.text_input("Enter first array: ")
input_b = st.text_input("Enter second array: ")

if input_a and input_b:
    try:
        arr_1 = np.array([int(i.strip()) for i in input_a.split(",")])
        arr_2 = np.array([int(i.strip()) for i in input_b.split(",")])

        st.write("First Array:", arr_1)
        st.write("Second Array:", arr_2)

        horizontal  = np.hstack((arr_1, arr_2))
        vertical = np.vstack((arr_1, arr_2))

        st.subheader("Horizontal Stack (hstack):")
        st.write(horizontal)

        st.subheader("Vertical Stack (vstack):")
        st.write(vertical)

    except:
        st.error("Enter Valid Input. Write numbers seperated by comma e.g. 1,2,3")