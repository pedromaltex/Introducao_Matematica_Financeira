APP_INFO = {
    "title": "💰 Compound Interest Calculator",
    "description": "Discover how your money grows with compound interest. "
    "Experiment with rates, periods, and contributions to see exponential growth in action."
}

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random as rd

if __name__=="__main__":
    from compound_interest import compounded_f_value, compounded_periodic_fvalue
else:
    from ..compound_interest.compound_interest import compounded_f_value, compounded_periodic_fvalue


def run():
    # --- Interface Streamlit ---
    st.title(APP_INFO["title"])


    # Inputs
    with st.sidebar.form("params_form"):

        st.header("Simulation Parameters")
        i_value = st.number_input("Initial Value $", 0, value=10000)

        contribuitions = st.number_input("Contribuitions $", 0, value=100)
        freq_contribuitions = st.radio("Frequency of Contributions:",
                                                ["Yearly", "Monthly", "Weekly"])

        anual_r = st.number_input("Anual Interest Rate %", min_value=0, value=7) / 100

        n_years = st.slider("Nº of Years", 1, 100, 20)
        submit = st.form_submit_button("Calculate")

    if submit:
        # --- Simulation ---
        fig = go.Figure()

        if freq_contribuitions == "Yearly":
            m_contribuitions = 1 # Number of Years in a Year
        elif freq_contribuitions == "Monthly":
            m_contribuitions = 12 # Number of Months in a Year
        else:
            m_contribuitions = 52 # Number of Weeks in a Year

        x_years = np.arange(1, n_years+1, 1)
        y = np.zeros(len(x_years))

        if contribuitions == 0:
            for year in x_years:
                y[year-1] = compounded_f_value(i_value, anual_r, year)

        elif contribuitions > 0:
            for year in x_years:
                y[year-1] = compounded_f_value(i_value, anual_r, year) + \
                compounded_periodic_fvalue(contribuitions, anual_r, m_contribuitions, year)
        else:
            st.error('Error. Contributions lower than 0.', icon="🚨")



        fig.add_trace(go.Scatter(
            x=x_years,
            y=y,
            mode='lines',
            name=f"Acumulated Value",
            opacity=0.7
        ))

        fig.add_trace(go.Bar(
            x=x_years,
            y=y,
            name=f"Accumulated Value",
            opacity=0.7
        ))

        fig.update_layout(
            title=f"Final Portfolio Value: {y[-1]:.2f}$",
            xaxis_title="Year",
            yaxis_title="Value",
            legend_title="Trajectory"
        )

        st.plotly_chart(fig)
        
if __name__=="__main__":
    run()

