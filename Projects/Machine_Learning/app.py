import streamlit as st
import pandas as pd
import joblib

model = joblib.load(r"C:\Users\prafu\Music\ML-Learning\ML-Playground\Projects\Machine_Learning\KNN_heart.pkl")
scaler = joblib.load(r"C:\Users\prafu\Music\ML-Learning\ML-Playground\Projects\Machine_Learning\scaler.pkl")
expected_columns = joblib.load(r"C:\Users\prafu\Music\ML-Learning\ML-Playground\Projects\Machine_Learning\columns.pkl")