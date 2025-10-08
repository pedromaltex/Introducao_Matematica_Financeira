APP_INFO = {
    "title": "Future Value of Money 💲",
    "description": "Explora a relação entre calls, puts, e o preço da ação subjacente."
}


import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random as rd
from ..future_value_of_money.compound_interest import decreasing_continuously_compounded


def run():

    # --- Interface Streamlit ---
    st.title("How much is 1💲 worth in the future?")

    # Inputs
    with st.sidebar.form("params_form"):

        st.header("Simulation Parameters")
        i_value = st.number_input("Initial Value $", 0, value=1)

        annual_r = st.number_input("Anual Interest Rate %", min_value=0, value=3) / 100

        n_years = st.slider("Nº of Years", 1, 100, 20)
        submit = st.form_submit_button("Calculate")

    if submit:
        # --- Simulation ---
        fig = go.Figure()

        x_years = np.arange(1, n_years+1, 1)
        y = np.zeros(len(x_years))


        for year in x_years:
            y[year-1] = decreasing_continuously_compounded(i_value, annual_r, year)



        fig.add_trace(go.Scatter(
            x=x_years,
            y=y,
            mode='lines',
            name=f"Decreasing Value",
            opacity=0.7
        ))

        fig.add_trace(go.Bar(
            x=x_years,
            y=y,
            name=f"Decreasing Value",
            opacity=0.7
        ))

        st.plotly_chart(fig)
        st.metric(f"Value in {n_years} years: ", f"${y[-1]:.2f}")

if __name__ == "__main__":
    run()
