import simulator, grn
import numpy as np


HA = grn.grn()

HA.add_input_species("X")
HA.add_input_species("Y")


HA.add_species("S", 0.1)
HA.add_species("C", 0.1)

regulators_sum_1 = [{'name': 'X', 'type': -1, 'Kd': 5, 'n': 2},
                    {'name': 'Y', 'type': 1, 'Kd': 5, 'n': 3}]
products_sum_1 = [{'name': 'S'}]
HA.add_gene(10, regulators_sum_1, products_sum_1)

regulators_sum_2 = [{'name': 'X', 'type': 1, 'Kd': 5, 'n': 2},
                    {'name': 'Y', 'type': -1, 'Kd': 5, 'n': 3}]
products_sum_2 = [{'name': 'S'}]
HA.add_gene(10, regulators_sum_2, products_sum_2)

regulators_carry = [{'name': 'X', 'type': 1, 'Kd': 5, 'n': 2},
                    {'name': 'Y', 'type': 1, 'Kd': 5, 'n': 2}]
products_carry = [{'name': 'C'}]
HA.add_gene(10, regulators_carry, products_carry,"and")

HA.plot_network()

T_HA, Y_HA = simulator.simulate_sequence(HA, [(0,0), (000,100), (100,0), (100,100)], t_single=300)

