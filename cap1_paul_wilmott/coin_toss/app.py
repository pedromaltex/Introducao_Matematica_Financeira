# app.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random as rd
from coin_toss import coin, geometric_random_walk, arithmetric_random_walk

"""
app.py
-------

Streamlit application for simulating and visualizing random walks.

This app allows the user to:
- Choose between Geometric and Arithmetic random walks.
- Define simulation parameters such as initial value, probability of upward movement,
  number of steps, and number of simulations.
- Visualize the resulting random walk trajectories interactively using Plotly.

Dependencies:
    - streamlit
    - numpy
    - plotly
    - coin_toss (custom module with random walk functions)
"""

# --- Interface Streamlit ---
st.title("Random Walk Simulator 🎲")

# Inputs
st.sidebar.header("Simulation Parameters")
initial_value = st.sidebar.number_input("Initial Value", 1, 1000, 100)
up_prob = st.sidebar.slider("Probabilidade de subida", 0.0, 1.0, 0.5)
steps = st.sidebar.slider("Nº of steps", 100, 5000, 1000)
simulations = st.sidebar.slider("Nº of simulations", 1, 20, 5)

walk_type = st.radio("Type of Random Walk:", 
                     ["Geometric", "Arithmetric"])

# --- Simulação ---
fig = go.Figure()

for i in range(simulations):
    if walk_type == "Geometric":
        y = geometric_random_walk(initial_value, up_prob, steps)
    else:
        y = arithmetric_random_walk(initial_value, up_prob, steps)

    fig.add_trace(go.Scatter(
        y=y,
        mode='lines',
        name=f"Simulation {i+1}",
        opacity=0.7
    ))

fig.update_layout(
    title=f"{walk_type} Random Walk ({simulations} Simulations)",
    xaxis_title="Steps",
    yaxis_title="Value",
    legend_title="Trajectory"
)

st.plotly_chart(fig)
