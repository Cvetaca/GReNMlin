import grn, simulator
import numpy as np
import matplotlib.pyplot as plt

my_grn = grn.grn()

my_grn.add_input_species("A")
my_grn.add_input_species("B")
my_grn.add_input_species("Cin")

my_grn.add_species("AxorB", 0.1)
my_grn.add_species("AxorBandCin", 0.1)
my_grn.add_species("AandB", 0.1)
my_grn.add_species("SUM", 0.1)
my_grn.add_species("Cout", 0.1)

AxorB = [{"name": "A", "type": -1, "Kd": 5, "n": 2},
              {"name": "B", "type": 1, "Kd": 5, "n": 2}]
AxorBout = [{"name": "AxorB"}]

my_grn.add_gene(10, AxorB, AxorBout)

AxorB_2 = [{"name": "A", "type": 1, "Kd": 5, "n": 2},
              {"name": "B", "type": -1, "Kd": 5, "n": 2}]
AxorBout_2 = [{"name": "AxorB"}]
my_grn.add_gene(10, AxorB_2, AxorBout_2)

AxorBCin = [{"name": "AxorB", "type": -1, "Kd": 5, "n": 2},
               {"name": "Cin", "type": 1, "Kd": 5, "n": 2}]
Sum = [{"name": "SUM"}]

my_grn.add_gene(10, AxorBCin, Sum)

AxorBCin_2 = [{"name": "AxorB", "type": 1, "Kd": 5, "n": 2},
               {"name": "Cin", "type": -1, "Kd": 5, "n": 2}]
Sum_2 = [{"name": "SUM"}]

my_grn.add_gene(10, AxorBCin_2, Sum_2)

AxorBandCin = [{"name": "AxorB", "type": 1, "Kd": 5, "n": 2},
              {"name": "Cin", "type": 1, "Kd": 5, "n": 2}]
AxorBandCinRes = [{"name": "AxorBandCin"}]
my_grn.add_gene(10, AxorBandCin, AxorBandCinRes, "and")

AandB = [{"name": "A", "type": 1, "Kd": 5, "n": 2},
                {"name": "B", "type": 1, "Kd": 5, "n": 2}]
AandBres = [{"name": "AandB"}]
my_grn.add_gene(10, AandB, AandBres, "and")

Cout = [{"name": "AandB", "type": 1, "Kd": 5, "n": 2}]
product5 = [{"name": "Cout"}]
my_grn.add_gene(10, Cout, product5)

regulators5 = [{"name": "AxorBandCin", "type": 1, "Kd": 5, "n": 2}]
product5 = [{"name": "Cout"}]
my_grn.add_gene(10, regulators5, product5)
print(my_grn.genes)
my_grn.plot_network()

"""T, Y = simulator.simulate_sequence(my_grn, [(0,0), (0,100), (100,0), (100,100)], t_single = 250)
plt.plot(T, Y[:, 2], label='AxorB')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()"""
T, Y = simulator.simulate_sequence(my_grn, [(0,0,0), (0,0,100), (0,100,0), (0,100,100), (100,0,0), (100,0,100), (100,100,0), (100,100,100)], t_single = 500)
#plt.plot(T, Y[:, 0], label='A')
#plt.plot(T, Y[:, 1], label='B')
plt.plot(T, Y[:, 7], label='Cout')
#plt.plot(T, Y[:, 2], label='Cin')
#plt.plot(T, Y[:, 3], label='AxorB')
plt.plot(T, Y[:, 6], label='SUM')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()