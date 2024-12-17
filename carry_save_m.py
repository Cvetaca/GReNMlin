import full_adder
import and_
import simulator, grn

#CSM == Carry Save Multiplier
CSM = grn.grn()

def int_to_binary(num):
    return format(num, 'b')

num1 = int(input("Vnesi 4 bitno stevilo: "))
num2 = int(input("Vnesi drugo 4 bitno stevilo: "))

X = int_to_binary(num1)
Y = int_to_binary(num2)

input_tuple = (0,) + tuple(int(bit)*100 for bit in X + Y)
print(input_tuple)

#4 bit multiplier
lenX = len(X)
lenY = len(Y)
lenOut = lenX + lenY

CSM.add_input_species("ZERO")

input_species = []

#Adding input species for A
for i in range(lenX,-1,-1):
    CSM.add_input_species("X"+str(i))
    input_species.append("X"+str(i))

#Adding input species for B
for i in range(lenY,-1,-1):
    CSM.add_input_species("Y"+str(i))
    input_species.append("Y"+str(i))

out_indexes = []

#print(input_species)
for i in range(lenX+1): #Iterating through the bits of B
    for j in range(lenY): #Iterating through the bits of A
        #print(i,j)
        #adding output species for the full adder
        CSM.add_species("POFAS"+str(i)+str(j), 0.1) #Partial Output Full Adder Sum
        CSM.add_species("POFAC"+str(i)+str(j), 0.1) #Partial Output Full Adder Carry
        if i==0: #first row only adds X0 with all Y bits
            spec = full_adder.full_adder(str(i)+str(j), "X"+str(i), "Y"+str(j), 
                                        "ZERO", "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
            out_indexes.append("POFAS"+str(i)+str(j))
        #For all other rows, we perform Xi and Yj and add the carry from the previous row and the sum from 
        #the previous row on j+1
        #The full adder takes X = Xi and Yi, Y = POFAS(i-1,j+i), Cin = POFAC(i-1,j)
        elif i > 0 and i < lenX+1:
            CSM.add_species("POA"+str(i)+str(j), 0.1) #Partial Output AND

            and_.and_("X"+str(i), "Y"+str(j), "POA"+str(i)+str(j), CSM) #AND gate betwee Xi and Yj

            if j == lenY-1: #If we are at the last bit of Y, the Y becomes ZERO
                spec = full_adder.full_adder(str(i)+str(j), "POA"+str(i)+str(j), "ZERO", "POFAC"+str(i-1)+str(j), 
                                        "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))
            else:
                spec = full_adder.full_adder(str(i)+str(j), "POA"+str(i)+str(j), "POFAS"+str(i-1)+str(j+1), 
                                        "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))
        elif i == lenX+1: #When we are past the last bit of X and i == 0, the X is ZERO

            if j == 0: #The X is ZERO
                spec = full_adder.full_adder(str(i)+str(j), "ZERO", "POFAS"+str(i-1)+str(j+1),
                                             "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))
            elif j == lenY-1: #If we are at the last bit of Y, the Y becomes ZERO, X is POFAC(i,j-1), Cin is POFAC(i-1,j)
                spec = full_adder.full_adder(str(i)+str(j), "POFAC"+str(i)+str(j-1), "ZERO", "POFAC"+str(i-1)+str(j), 
                                        "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))
            else:
                spec = full_adder.full_adder(str(i)+str(j), "POFAC"+str(i)+str(j-1), "POFAS"+str(i-1)+str(j+1), "POFAC"+str(i-1)+str(j), 
                                        "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))

T_FA, Y_FA = simulator.simulate_single(CSM, input_tuple,t_end=1000)

final_output=[]
for a in out_indexes:
    if Y_FA[:, CSM.species_names.index(a)][-1]>50:
        final_output.append(str(1))
    else:
        final_output.append(str(0))
print("Binarni izhod:","".join(final_output)[::-1],"Decimalni izhod:",int("".join(final_output)[::-1], 2))

                                             
