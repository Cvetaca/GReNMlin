import grn
import simulator
from full_adder import full_adder
import matplotlib.pyplot as plt

def carry_save_n_bit_adder(grn_model, n):

    # Define the input species for the n-bit numbers
    for i in range(n):
        grn_model.add_input_species(f"A{i}")
        grn_model.add_input_species(f"B{i}")
        grn_model.add_input_species(f"C{i}")

    # Define intermediate and output species
    for i in range(n):
        grn_model.add_species(f"SUM{i}", 0.1)  # Partial sum
        grn_model.add_species(f"Cout{i}", 0.1)  # Carry out
    grn_model.add_species(f"FinalCarry", 0.1)  # Final carry for nth bit
    grn_model.add_species(f"ZERO", 0.1)  # Zero species
    grn_model.add_species(f"Cin", 0.1)  # Carry in

    # Chain full adders for carry-save addition
    for i in range(n):
        if i == 0:
            # First stage, no carry input (Cin=0)
            full_adder(i, f"A{i}", f"B{i}", "ZERO", f"SUM{i}", f"Cout{i}", grn_model, zero=True)
        else:
            # Subsequent stages use carry from previous stage
            full_adder(i, f"A{i}", f"B{i}", f"Cout{i-1}", f"SUM{i}", f"Cout{i}", grn_model, zero=False)

    # Resolve final carry into the n+1th bit (if needed)
    grn_model.add_gene(
        10, 
        [{'name': f'Cout{n-1}', 'type': 1, 'Kd': 5, 'n': 3}], 
        [{'name': 'FinalCarry'}], 
        logic_type='or'
    )

if __name__ == "__main__":
    n = 2  
    CSA_GRN = grn.grn()

    carry_save_n_bit_adder(CSA_GRN, n)

    import itertools
    #input_sequence = list(itertools.product([0, 100], repeat=3 * n))  # All combinations for 3 n-bit numbers
        # Define specific binary inputs for A=01 and B=00
    A_binary = [0, 0]  # Binary '01': A1=0, A0=100
    B_binary = [0, 0]    # Binary '00': B1=0, B0=0
    C_binary = [0, 0]    # Binary '00': Initial carry input is zero

    # Flatten the inputs to match the simulation format
    input_sequence = [A_binary + B_binary + C_binary]

    # Simulate the sequence
    T_CSA, Y_CSA = simulator.simulate_sequence(CSA_GRN, input_sequence, t_single=500)
    #T_CSA, Y_CSA = simulator.simulate_sequence(CSA_GRN, input_sequence, t_single=500)
    # Plot outputs
    #CSA_GRN.plot_network()

    plt.plot(T_CSA, Y_CSA[:, 0], label=f'A0')
    plt.plot(T_CSA, Y_CSA[:, 1], label=f'B0') 
    #plt.plot(T_CSA, Y_CSA[:, 3], label=f'A1')
    #plt.plot(T_CSA, Y_CSA[:, 4], label=f'B1')

    # Plot selected output variables
    #for i in range(n):
        #plt.plot(T_CSA, Y_CSA[:, 0], label=f'A0')
        #plt.plot(T_CSA, Y_CSA[:, 1], label=f'B0') 
        #plt.plot(T_CSA, Y_CSA[:, 3], label=f'A1')
        #plt.plot(T_CSA, Y_CSA[:, 4], label=f'B1')
    #plt.plot(T_CSA, Y_CSA[:, -1], label='FinalCarry')  # Adjust for the final carry variable
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.legend()
    plt.show()
