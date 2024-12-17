import simulator, grn
import numpy as np


def full_adder(id,X,Y,Cin,SUM,Cout,FA: grn.grn):
    #all_species = []
    FA.add_species("O1"+str(id), 0.1)
    FA.add_species("O2"+str(id), 0.1)
    FA.add_species("O3"+str(id), 0.1)
    #all_species.append("O1"+str(id))
    #all_species.append("O2"+str(id))
    #all_species.append("O3"+str(id))
    
    

    #A XOR B  = O1
    AxorB = [{'name': X, 'type': -1, 'Kd': 5, 'n': 2},
            {'name': Y, 'type': 1, 'Kd': 5, 'n': 3}]
    ResAxorB = [{'name': 'O1'+str(id)}]
    FA.add_gene(10, AxorB, ResAxorB)

    AxorB_2 = [{'name': X, 'type': 1, 'Kd': 5, 'n': 2},
                {'name': Y, 'type': -1, 'Kd': 5, 'n': 3}]
    ResAxorB_2 = [{'name': 'O1'+str(id)}]
    FA.add_gene(10, AxorB_2, ResAxorB_2)

    # O1 XOR Cin = SUM

    SxorCin = [{'name': 'O1'+str(id), 'type': -1, 'Kd': 5, 'n': 2},
                {'name': Cin, 'type': 1, 'Kd': 5, 'n': 3}]
    ResSxorCin = [{'name': SUM}]
    FA.add_gene(10, SxorCin, ResSxorCin)

    SxorCin_2 = [{'name': 'O1'+str(id), 'type': 1, 'Kd': 5, 'n': 2},
                {'name': Cin, 'type': -1, 'Kd': 5, 'n': 3}]
    ResSxorCin_2 = [{'name': SUM}]
    FA.add_gene(10, SxorCin_2, ResSxorCin_2)

    # O1 AND Cin = O2

    SandCin = [{'name': 'O1'+str(id), 'type': 1, 'Kd': 5, 'n': 2},
                        {'name': Cin, 'type': 1, 'Kd': 5, 'n': 3}]
    ResSandCin = [{'name': 'O2'+str(id)}]
    FA.add_gene(10, SandCin, ResSandCin,"and")

    # X_FA AND Y_FA = O3

    XandY = [{'name': X, 'type': 1, 'Kd': 5, 'n': 2},
                        {'name': Y, 'type': 1, 'Kd': 5, 'n': 3}]
    ResXandY = [{'name': 'O3'+str(id)}]
    FA.add_gene(10, XandY, ResXandY,"and")

    #O2 or O3 = Cout
    O2orO3 = [{'name': 'O2'+str(id), 'type': 1, 'Kd': 5, 'n': 2},
                        {'name': 'O3'+str(id), 'type': 1, 'Kd': 5, 'n': 3}]
    ResO2orO3 = [{'name': Cout}]
    FA.add_gene(10, O2orO3, ResO2orO3,"or")
    #return all_species
    FA.genes

if __name__=="__main__":
    FA=grn.grn()

    FA.add_input_species("A")
    FA.add_input_species("B")
    FA.add_input_species("Cin")
    FA.add_species("SUM", 0.1)
    FA.add_species("Cout", 0.1)
    full_adder(1,"A","B","Cin","SUM","Cout",FA)
    import matplotlib.pyplot as plt
    FA.plot_network
    T_FA, Y_FA = simulator.simulate_sequence(FA, [(0,0,0),(0,0,100),(0,100,0),(0,100,100),(100,0,0),(100,0,100),(100,100,0),(100,100,100)], t_single=500)
    print(len(Y_FA[0]))
    plt.plot(T_FA, Y_FA[:, 4], label='Cout')
    plt.plot(T_FA, Y_FA[:, 3], label='SUM')
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.legend()
    plt.show()
