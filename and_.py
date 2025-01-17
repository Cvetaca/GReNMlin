import simulator, grn
import numpy as np


def and_(in1,in2,out,FA: grn.grn):

    AandB = [{'name':in1, 'type': 1, 'Kd': 5, 'n': 2},
            {'name': in2, 'type': 1, 'Kd': 5, 'n': 2}]
    
    ResAandB = [{'name': out}]

    FA.add_gene(10, AandB, ResAandB,"and")

if __name__ =="__main__":
    FA=grn.grn()

    FA.add_input_species("A")
    FA.add_input_species("B")
    FA.add_species("OUT", 0.1)
    and_("A","B","OUT",FA)
    import matplotlib.pyplot as plt
    FA.plot_network
    T_FA, Y_FA = simulator.simulate_sequence(FA, [(0,0),(0,100),(100,0),(100,100)],t_single=250)
    plt.plot(T_FA,Y_FA)
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.legend()
    plt.show()