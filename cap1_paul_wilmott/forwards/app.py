import streamlit as st
import numpy as np
import plotly.graph_objects as go
from forward_aux import no_arbitrage_forward

# --- Interface Streamlit ---
st.title("Forwards - Arbitrage or No Arbitrage??")

st.info(
    """
    **Instructions**

    - Guess the forward contract's fair value  
    - The no-arbitrage condition is given by: $$ F = S(0) \, e^{r(T - t)} $$

    - Decide whether there is an **arbitrage opportunity**
    """
)

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
    monthly_r = annual_r / 100 / 12   # % → decimal

    F_market = st.number_input(
        "Forward Price (Market) [F]", 
        min_value=0.00, 
        step=0.10, 
        value=105.00, 
        format="%.2f"
    )

    n_months = st.slider("Maturity (months)", 1, 540, 12)
    submit = st.form_submit_button("Calculate")

if submit:
    # --- Simulação do forward teórico ---
    x_months = np.arange(1, n_months + 1)
    y_forward = [no_arbitrage_forward(spot_0, monthly_r, t) for t in x_months]

    # --- Forward teórico no vencimento ---
    F_theoretical = round(y_forward[-1], 2)

    # --- Verificação de arbitragem ---
    tolerance = 0.000001 * F_theoretical  

    if abs(F_market - F_theoretical) <= tolerance:
        arbitrage_msg = "✅ No Arbitrage (fair price within tolerance)"
        strategy = "Do nothing"
    elif F_market > F_theoretical:
        arbitrage_msg = "📈 Arbitrage Opportunity: SELL Forward"
        strategy = (
            "- Short the forward contract\n"
            "- Buy the asset in the spot market\n"
            "- Finance purchase at risk-free rate"
        )
    else:
        arbitrage_msg = "📉 Arbitrage Opportunity: BUY Forward"
        strategy = (
            "- Long the forward contract\n"
            "- Short the asset in the spot market\n"
            "- Invest proceeds at risk-free rate"
        )

    # --- Gráfico ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_months, 
        y=y_forward, 
        mode='lines', 
        name="Forward (No Arbitrage)",
    ))

    fig.add_trace(go.Scatter(
        x=[n_months], 
        y=[F_market], 
        mode='markers', 
        marker=dict(size=12, color="yellow"), 
        name="Forward (Market)"
    ))

    fig.add_trace(go.Scatter(
        x=[n_months], 
        y=[F_theoretical], 
        mode='markers', 
        marker=dict(size=12, color="blue"), 
        name="Forward (Theoretical)"
    ))
    # --- Layout “full” ---
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),  # remove margens
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    # --- Métricas ---
    st.info(
        f"- Theoretical Forward Price ${F_theoretical:.2f}\n"
        f" - Market Forward Price ${F_market:.2f}"
    )

    if strategy != "Do nothing":
        success_message = f"{arbitrage_msg}\n" + f"\n**Suggested Arbitrage Strategy:**\n{strategy}"
        st.success(success_message)
    else:
        st.success(f"{arbitrage_msg}\n")

