import full_adder
import half_adder
import group_out
import and_
import simulator, grn
import random
from collections import Counter
AM=grn.grn()
#full_adder.full_adder(1,test)



def int_to_binary(num):
    return format(num, 'b')


num1 = int(input("Vnesi n bitno stevilo: "))
num2 = int(input("Vnesi drugo m bitno stevilo: "))

bin_num1 = int_to_binary(num1)
bin_num2 = int_to_binary(num2)

lenA=len(bin_num1)
lenB=len(bin_num2)
lenOut=lenA+lenB


input_tuple = (0,) + tuple(int(bit)*100 for bit in bin_num1 + bin_num2)
print(input_tuple)

AM.add_input_species("ZERO")
#all_species=[]
for i in range(lenA-1,-1,-1):
    AM.add_input_species("A"+str(i))
    #all_species.append("A"+str(i))
for i in range(lenB-1,-1,-1):
    AM.add_input_species("B"+str(i))
    #all_species.append("B"+str(i))
out_indexes=[]
for j in range(lenA):
    AM.add_species("POFAS0"+str(j), 0.1)
    #all_species.append("POFAS0"+str(j))
    and_.and_("A"+str(j),"B0","POFAS0"+str(j),AM)
    if j==0:
        out_indexes.append("POFAS00")
        #print("Grouped on OUT0")
        
for i in range(1,lenB):
    for j in range(lenA):
        AM.add_species("POA"+str(i)+str(j), 0.1)
        #all_species.append("POA"+str(i)+str(j))
        and_.and_("A"+str(j),"B"+str(i),"POA"+str(i)+str(j),AM)
        AM.add_species("POFAS"+str(i)+str(j), 0.1)
        #all_species.append("POFAS"+str(i)+str(j))
        AM.add_species("POFAC"+str(i)+str(j), 0.1)
        #all_species.append("POFAC"+str(i)+str(j))
        if j==0:
            #print(f"J=0     IN POPOFAS{i-1}{j+1} POA{i}{j} ZERO OUT: POFAS{i}{j} POFAC{i}{j}")
            spec=full_adder.full_adder(str(i)+str(j),"POFAS"+str(i-1)+str(j+1),"POA"+str(i)+str(j),"ZERO","POFAS"+str(i)+str(j),"POFAC"+str(i)+str(j),AM)
            #all_species.extend(spec)
            #group_out.group_out("POFAS"+str(i)+str(j),"OUT"+str(i),"OUT"+str(i),AM)
            out_indexes.append("POFAS"+str(i)+str(j))
            #print("Grouped on OUT"+str(i))
        elif j==lenA-1 and i==1:
            #print(f"J=kon  IN ZERO POA{i}{j} POFAC{i}{j-1} OUT POFAS{i}{j} POFAC{i}{j}")
            spec=full_adder.full_adder(str(i)+str(j),"ZERO","POA"+str(i)+str(j),"POFAC"+str(i)+str(j-1),"POFAS"+str(i)+str(j),"POFAC"+str(i)+str(j),AM)
            #all_species.extend(spec)
        elif j==lenA-1 and i!=1:
            spec=full_adder.full_adder(str(i)+str(j),"POFAC"+str(i-1)+str(j),"POA"+str(i)+str(j),"POFAC"+str(i)+str(j-1),"POFAS"+str(i)+str(j),"POFAC"+str(i)+str(j),AM)
        else:
            #print(f"J={j}   IN PO{i}{j} POA{i}{j} POFAC{i}{j-1} OUT POFAS{i}{j} POFAC{i}{j}")
            spec=full_adder.full_adder(str(i)+str(j),"POFAS"+str(i-1)+str(j+1),"POA"+str(i)+str(j),"POFAC"+str(i)+str(j-1),"POFAS"+str(i)+str(j),"POFAC"+str(i)+str(j),AM)
            #all_species.extend(spec)
        if i==lenB-1 and j!=0:
            #group_out.group_out("POFAS"+str(i)+str(j),"OUT"+str(i+j),"OUT"+str(i+j),AM)
            #print("Added POFAS"+str(i)+str(j)+" to OUT"+str(i+j))
            out_indexes.append("POFAS"+str(i)+str(j))
            #print("Grouped on OUT"+str(i+j))
        if i==lenB-1 and j==lenA-1:
            #group_out.group_out("POFAC"+str(i)+str(j),"OUT"+str(i+j+1),"OUT"+str(i+j+1),AM)
            #print("Added POFAC"+str(i)+str(j)+" to OUT"+str(i+j+1))
            out_indexes.append("POFAC"+str(i)+str(j))
            #print("Grouped on OUT"+str(i+j+1))


T_FA, Y_FA = simulator.simulate_single(AM, input_tuple,t_end=1000)

final_output=[]
for a in out_indexes:
    if Y_FA[:, AM.species_names.index(a)][-1]>50:
        final_output.append(str(1))
    else:
        final_output.append(str(0))
print("Binarni izhod:","".join(final_output)[::-1],"Decimalni izhod:",int("".join(final_output)[::-1], 2))

