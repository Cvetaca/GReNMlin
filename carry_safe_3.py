import full_adder
import and_
import simulator, grn

AM = grn.grn()

def int_to_binary(num):
    return format(num, 'b')

num1 = int(input("Vnesi n bitno stevilo: "))
num2 = int(input("Vnesi drugo m bitno stevilo: "))

bin_num1 = int_to_binary(num1)
bin_num2 = int_to_binary(num2)

lenA = len(bin_num1)
lenB = len(bin_num2)
lenOut = lenA + lenB

input_tuple = (0,) + tuple(int(bit) * 100 for bit in bin_num1 + bin_num2)
print(input_tuple)

AM.add_input_species("ZERO")

for i in range(lenA - 1, -1, -1):
    AM.add_input_species("A" + str(i))

for i in range(lenB - 1, -1, -1):
    AM.add_input_species("B" + str(i))

out_indexes = []
for j in range(lenA):
    AM.add_species("POFAS0" + str(j), 0.1)
    and_.and_("A" + str(j), "B0", "POFAS0" + str(j), AM)
    if j == 0:
        out_indexes.append("POFAS00")

for i in range(1, lenB):
    for j in range(lenA):
        AM.add_species("POA" + str(i) + str(j), 0.1)
        and_.and_("A" + str(j), "B" + str(i), "POA" + str(i) + str(j), AM)
        AM.add_species("POFAS" + str(i) + str(j), 0.1)
        AM.add_species("POFAC" + str(i) + str(j), 0.1)

        if j == 0:
            # First column: CIN is ZERO
            spec = full_adder.full_adder(str(i) + str(j), "POFAS" + str(i - 1) + str(j + 1), "POA" + str(i) + str(j), "ZERO", "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM); out_indexes.append("POFAS" + str(i) + str(j))
        elif j == lenA - 1:
            # Last column: CIN is the COUT of the previous row
            spec = full_adder.full_adder(str(i) + str(j), "ZERO" if i == 1 else "POFAC" + str(i - 1) + str(j), "POA" + str(i) + str(j), "POFAC" + str(i) + str(j - 1), "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
        else:
            # General case: CIN is the diagonal COUT from the previous row
            spec = full_adder.full_adder(str(i) + str(j), "POFAS" + str(i - 1) + str(j + 1), "POA" + str(i) + str(j), "POFAC" + str(i) + str(j - 1), "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
        if i == lenB - 1 and j != 0:
            out_indexes.append("POFAS" + str(i) + str(j))
        if i == lenB - 1 and j == lenA - 1:
            out_indexes.append("POFAC" + str(i) + str(j))

T_FA, Y_FA = simulator.simulate_single(AM, input_tuple, t_end=1000)

final_output = []
for a in out_indexes:
    if Y_FA[:, AM.species_names.index(a)][-1] > 50:
        final_output.append(str(1))
    else:
        final_output.append(str(0))
print("Binarni izhod:", "".join(final_output)[::-1], "Decimalni izhod:", int("".join(final_output)[::-1], 2))
