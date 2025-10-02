import streamlit as st
import numpy as np
import plotly.graph_objects as go
from forward_aux import no_arbitrage_forward

# --- Interface Streamlit ---
st.title("Forwards - Arbitrage or No Arbitrage??")

# Inputs
with st.sidebar.form("params_form"):
    st.header("Parameters")    

    spot_0 = st.number_input(
        label="Spot Asset Price $ [S(0)]", 
        step=0.1, 
        format="%.2f", 
        value=100.0
    )

    annual_r = st.number_input(
        "Annual Interest Rate % [r]", 
        min_value=0.0, 
        step=0.1, 
        value=5.0, 
        format="%.2f"
    )
    monthly_r = annual_r / 100 / 12   # convertendo de % para decimal

    F_market = st.number_input(
        "Forward Price (Market) [F]", 
        min_value=0.0, 
        step=0.1, 
        value=105.0, 
        format="%.2f"
    )

    n_months = st.slider("Maturity (months)", 1, 540, 12)
    submit = st.form_submit_button("Calculate")

if submit:
    # --- Simulação do forward teórico ---
    x_months = np.arange(1, n_months + 1)
    y_forward = [no_arbitrage_forward(spot_0, monthly_r, t) for t in x_months]

    # --- Forward teórico no vencimento ---
    F_theoretical = y_forward[-1]

    # --- Verificação de arbitragem ---
    arbitrage_msg = ""
    if np.isclose(F_market, F_theoretical, atol=1e-2):
        arbitrage_msg = "✅ No Arbitrage (preço justo) (Approximation)"
    elif F_market > F_theoretical:
        arbitrage_msg = "📈 Arbitrage Opportunity: SELL Forward"
    else:
        arbitrage_msg = "📉 Arbitrage Opportunity: BUY Forward"

    # --- Gráfico ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_months, 
        y=y_forward, 
        mode='lines', 
        name="Forward (No Arbitrage)"    
        ))

    fig.add_trace(go.Scatter(
        x=[n_months], 
        y=[F_market], 
        mode='markers', 
        marker=dict(size=12, color="yellow"), 
        name="Forward (Market)"
    ))

    st.plotly_chart(fig)

    # --- Métricas ---
    st.metric("Theoretical Forward Price", f"${F_theoretical:.2f}")
    st.metric("Market Forward Price", f"${F_market:.2f}")
    st.success(arbitrage_msg)
