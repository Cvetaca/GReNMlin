import simulator, grn
import numpy as np

def half_adder(id,HA: grn.grn):
    HA.add_input_species("X_HA"+str(id))
    HA.add_input_species("Y_HA"+str(id))


    HA.add_species("S"+str(id), 0.1)
    HA.add_species("C"+str(id), 0.1)

    regulators_sum_1 = [{'name': 'X_HA'+str(id), 'type': -1, 'Kd': 5, 'n': 2},
                        {'name': 'Y_HA'+str(id), 'type': 1, 'Kd': 5, 'n': 3}]
    products_sum_1 = [{'name': 'S'+str(id)}]
    HA.add_gene(10, regulators_sum_1, products_sum_1)

    regulators_sum_2 = [{'name': 'X_HA'+str(id), 'type': 1, 'Kd': 5, 'n': 2},
                        {'name': 'Y_HA'+str(id), 'type': -1, 'Kd': 5, 'n': 3}]
    products_sum_2 = [{'name': 'S'+str(id)}]
    HA.add_gene(10, regulators_sum_2, products_sum_2)

    regulators_carry = [{'name': 'X_HA'+str(id), 'type': 1, 'Kd': 5, 'n': 2},
                        {'name': 'Y_HA'+str(id), 'type': 1, 'Kd': 5, 'n': 2}]
    products_carry = [{'name': 'C'+str(id)}]
    HA.add_gene(10, regulators_carry, products_carry,"and")

if __name__=="__main__":
    
    HA = grn.grn()
    half_adder(1,HA)
    HA.plot_network()

    T_HA, Y_HA = simulator.simulate_sequence(HA, [(0,0), (000,100), (100,0), (100,100)], t_single=500)
    import matplotlib.pyplot as plt

    plt.plot(T_HA, Y_HA[:, 3], label='Cout')
    plt.plot(T_HA, Y_HA[:, 2], label='SUM')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.legend()
    plt.show()

