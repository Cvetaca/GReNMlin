import full_adder
import half_adder
import group_out
import and_
import simulator, grn
import random
from collections import Counter

AM = grn.grn()

lenA = 4
lenB = 4
lenOut = lenA + lenB

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
            spec = full_adder.full_adder(str(i) + str(j), "POFAS" + str(i - 1) + str(j + 1), "POA" + str(i) + str(j), "ZERO", "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
            out_indexes.append("POFAS" + str(i) + str(j))
        elif j == lenA - 1 and i == 1:
            spec = full_adder.full_adder(str(i) + str(j), "ZERO", "POA" + str(i) + str(j), "POFAC" + str(i) + str(j - 1), "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
        elif j == lenA - 1 and i != 1:
            spec = full_adder.full_adder(str(i) + str(j), "POFAC" + str(i - 1) + str(j), "POA" + str(i) + str(j), "POFAC" + str(i) + str(j - 1), "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
        else:
            spec = full_adder.full_adder(str(i) + str(j), "POFAS" + str(i - 1) + str(j + 1), "POA" + str(i) + str(j), "POFAC" + str(i) + str(j - 1), "POFAS" + str(i) + str(j), "POFAC" + str(i) + str(j), AM)
        if i == lenB - 1 and j != 0:
            out_indexes.append("POFAS" + str(i) + str(j))
        if i == lenB - 1 and j == lenA - 1:
            out_indexes.append("POFAC" + str(i) + str(j))

def int_to_4bit_binary(num):
    return format(num, '04b')

num1 = int(input("Vnesi 4 bitno stevilo (0-15): "))
num2 = int(input("Vnesi drugo 4 bitno stevilo (0-15): "))

bin_num1 = int_to_4bit_binary(num1)
bin_num2 = int_to_4bit_binary(num2)

input_tuple = (0,) + tuple(int(bit) * 100 for bit in bin_num1 + bin_num2)
print(input_tuple)
T_FA, Y_FA = simulator.simulate_single(AM, input_tuple, t_end=4000)

final_output = []
for a in out_indexes:
    if Y_FA[:, AM.species_names.index(a)][-1] > 20:
        final_output.append(str(1))
    else:
        final_output.append(str(0))
print("Binarni izhod:", "".join(final_output)[::-1], "Decimalni izhod:", int("".join(final_output)[::-1], 2))
