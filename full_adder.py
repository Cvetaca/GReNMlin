import simulator, grn
import numpy as np
FA=grn.grn()

FA.add_input_species("X")
FA.add_input_species("Y")
FA.add_input_species("Cin")

FA.add_species("S", 0.1)
FA.add_species("Cout", 0.1)
FA.add_species("SUM", 0.1)
FA.add_species("O2", 0.1)
FA.add_species("O3", 0.1)

#A XOR B  = S
AxorB = [{'name': 'X', 'type': -1, 'Kd': 5, 'n': 2},
        {'name': 'Y', 'type': 1, 'Kd': 5, 'n': 3}]
ResAxorB = [{'name': 'S'}]
FA.add_gene(10, AxorB, ResAxorB)

AxorB_2 = [{'name': 'X', 'type': 1, 'Kd': 5, 'n': 2},
            {'name': 'Y', 'type': -1, 'Kd': 5, 'n': 3}]
ResAxorB_2 = [{'name': 'S'}]
FA.add_gene(10, AxorB_2, ResAxorB_2)

# S XOR Cin = SUM

SxorCin = [{'name': 'S', 'type': -1, 'Kd': 5, 'n': 2},
            {'name': 'Cin', 'type': 1, 'Kd': 5, 'n': 3}]
ResSxorCin = [{'name': 'SUM'}]
FA.add_gene(10, SxorCin, ResSxorCin)

SxorCin_2 = [{'name': 'S', 'type': 1, 'Kd': 5, 'n': 2},
            {'name': 'Cin', 'type': -1, 'Kd': 5, 'n': 3}]
ResSxorCin_2 = [{'name': 'SUM'}]
FA.add_gene(10, SxorCin_2, ResSxorCin_2)

# S AND Cin = O2

SandCin = [{'name': 'S', 'type': 1, 'Kd': 5, 'n': 2},
                    {'name': 'Cin', 'type': 1, 'Kd': 5, 'n': 3}]
ResSandCin = [{'name': 'O2'}]
FA.add_gene(10, SandCin, ResSandCin,"and")

# X AND Y = O3

XandY = [{'name': 'X', 'type': 1, 'Kd': 5, 'n': 2},
                    {'name': 'Y', 'type': 1, 'Kd': 5, 'n': 3}]
ResXandY = [{'name': 'O3'}]
FA.add_gene(10, XandY, ResXandY,"and")

#O2 or O3 = Cout
O2orO3 = [{'name': 'O2', 'type': 1, 'Kd': 5, 'n': 2},
                     {'name': 'O3', 'type': 1, 'Kd': 5, 'n': 3}]
ResO2orO3 = [{'name': 'Cout'}]
FA.add_gene(10, O2orO3, ResO2orO3,"or")

#FA.plot_network()
FA.plot_network
T_FA, Y_FA = simulator.simulate_sequence(FA, [(0,0,0),(0,0,100),(0,100,0),(0,100,100),(100,0,0),(100,0,100),(100,100,0),(100,100,100)], t_single=500)
print(len(Y_FA[0]))


#(100,0,0),(0,100,0) NE DELA


import matplotlib.pyplot as plt

plt.plot(T_FA, Y_FA[:, 3], label='S')
plt.plot(T_FA, Y_FA[:, 5], label='SUM')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()
