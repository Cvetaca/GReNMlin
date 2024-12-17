import grn, simulator
import numpy as np

my_grn = grn.grn()

my_grn.add_input_species("A")
my_grn.add_input_species("B")
my_grn.add_species("C", 0.1)
my_grn.add_species("D", 0.1)

regulators = [{"name": "A", "type": 1, "Kd": 5, "n": 2}, 
              {"name": "B", "type": -1, "Kd": 5, "n": 2}]
products = [{"name": "C"}]

my_grn.add_gene(10, regulators, products)

regulators = [{"name": "A", "type": -1, "Kd": 5, "n": 2}, 
              {"name": "B", "type": 1, "Kd": 5, "n": 2}]
products = [{"name": "C"}]

my_grn.add_gene(10, regulators, products)

regulators = [{"name": "C", "type": -1, "Kd": 5, "n": 2}]

products = [{"name": "D"}]

my_grn.add_gene(10, regulators, products)

my_grn.plot_network()

T, Y = simulator.simulate_sequence(my_grn, [(0,0), (0,100), (100,0), (100,100)], t_single = 250)