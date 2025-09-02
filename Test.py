import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Simple Streamlit App")

# Text input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")

# Slider
number = st.slider("Select a number", 1, 100, 25)
st.write(f"You selected: {number}")

# Generate random data
data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["X", "Y"]
)

# Show chart
st.line_chart(data)
