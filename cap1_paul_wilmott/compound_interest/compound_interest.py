
def compounded_f_value(i_v, annual_r, t):
    f = i_v * (1 + annual_r) ** (t)
    return f

def compounded_periodic_fvalue(payment, annual_r, m, t):
    """
    Calcula o valor futuro de aportes recorrentes (anuidade).
    
    payment: aporte periódico
    r: taxa de juros por período
    m: número de capitalizações por ano
    t: número de anos
    """
    r = annual_r/m
    n = m * t # número total de períodos

    # é a formula da soma geométrica de FV=P⋅[(1+i)**(n−1)+(1+i)**(n−2)+⋯+(1+i)**1+1]
    fv = payment * ((1 + r)**n - 1) / r 
    return fv

