def no_arbitrage_forward(spot: float, r: float, T: int) -> float:
    """
    Calcula o preço forward sem arbitragem.
    
    spot: preço à vista (S0)
    r: taxa de juros mensal (em decimal, ex: 0.01 = 1%)
    T: prazo em meses
    """
    return spot * (1 + r) ** T

