import grn
import numpy as np
import simulator

my_grn = grn.grn()

my_grn.add_input_species('A')
my_grn.add_input_species('B')
my_grn.add_species('C', 0.1)
my_grn.add_species('D', 0.1)

AandB = [{'name': 'A', 'type': 1, 'Kd': 5, 'n': 2}, {'name': 'B', 'type': 1, 'Kd': 5, 'n': 2}]
aRes = [{'name': 'C'}]

my_grn.add_gene(10, AandB, aRes)

neg = [{'name': 'C', 'type': -1, 'Kd': 5, 'n': 2}]
negRes= [{'name': 'D'}]

my_grn.add_gene(10, neg, negRes)

print(my_grn.genes)

my_grn.plot_network()

T, Y = simulator.simulate_sequence(my_grn, [(0,0), (0,100), (100,0), (100,100)], t_single = 250)