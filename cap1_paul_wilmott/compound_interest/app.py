import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random as rd
from compound_interest import compounded_f_value, compounded_periodic_fvalue

# --- Interface Streamlit ---
st.title("Compound Interest Calculator")


# Inputs
with st.sidebar.form("params_form"):

    st.header("Simulation Parameters")
    i_value = st.number_input("Initial Value")

    contribuitions = st.number_input("Contribuitions")
    freq_contribuitions = st.radio("Frequency of Contributions:",
                                            ["Yearly", "Monthly", "Weekly"])

    r = st.number_input("Interest Rate")
    freq_r = st.radio("Frequency of Interest Rate:",
                            ["Yearly", "Monthly", "Weekly"])

    n_years = st.slider("Nº of Years", 1, 40, 1)
    submit = st.form_submit_button("Calculate")

# --- Simulação ---
fig = go.Figure()

if freq_r == "Yearly":
    r = r
elif freq_r == "Monthly":
    r /= 12
else:
    r /= 52


if freq_contribuitions == "Yearly":
    m_contribuitions = 1 # Number of Years in a Year
elif freq_contribuitions == "Monthly":
    m_contribuitions = 12 # Number of Months in a Year
else:
    m_contribuitions = 52 # Number of Weeks in a Year

x_years = np.arange(1, n_years+1, 1)
y = np.zeros(len(x_years))
print(y)

if contribuitions == 0:
    for year in x_years:
        y[year-1] = compounded_f_value(i_value, r, year)

elif contribuitions > 0:
    for year in x_years:
        y[year-1] = compounded_f_value(i_value, r, year) + \
        compounded_periodic_fvalue(contribuitions, r, m_contribuitions, year)
else:
    st.error('Error. Contributions lower than 0.', icon="🚨")



fig.add_trace(go.Scatter(
    x=x_years,
    y=y,
    mode='lines',
    name=f"Acumulated Value",
    opacity=0.7
))

fig.update_layout(
    title=f"Final Portfolio Value",
    xaxis_title="Steps",
    yaxis_title="Value",
    legend_title="Trajectory"
)

st.plotly_chart(fig)

