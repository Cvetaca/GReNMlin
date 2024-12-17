import numpy as np 

def solve_model(T,state):
    A, B, Cin, AxorB, AxorBandCin, AandB, SUM, Cout = state
    dA = -A*0
    dB = -B*0
    dCin = -Cin*0
    dAxorB = -AxorB*0.1+10*(((B/5)**2))/(1+((A/5)**2)+((B/5)**2)+((A/5)**2)*((B/5)**2))+10*(((A/5)**2))/(1+((A/5)**2)+((B/5)**2)+((A/5)**2)*((B/5)**2))
    dAxorBandCin = -AxorBandCin*0.1+10*(((AxorB/5)**2)*((Cin/5)**2))/(1+((AxorB/5)**2)+((Cin/5)**2)+((AxorB/5)**2)*((Cin/5)**2))
    dAandB = -AandB*0.1+10*(((A/5)**2)*((B/5)**2))/(1+((A/5)**2)+((B/5)**2)+((A/5)**2)*((B/5)**2))
    dSUM = -SUM*0.1+10*(((Cin/5)**2))/(1+((AxorB/5)**2)+((Cin/5)**2)+((AxorB/5)**2)*((Cin/5)**2))+10*(((AxorB/5)**2))/(1+((AxorB/5)**2)+((Cin/5)**2)+((AxorB/5)**2)*((Cin/5)**2))
    dCout = -Cout*0.1+10*(((AandB/5)**2))/(1+((AandB/5)**2))+10*(((AxorBandCin/5)**2))/(1+((AxorBandCin/5)**2))
    return np.array([dA, dB, dCin, dAxorB, dAxorBandCin, dAandB, dSUM, dCout])

def solve_model_steady(state):
    return solve_model(0, state)
