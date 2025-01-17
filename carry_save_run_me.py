import full_adder
import and_
import simulator, grn

CSM = grn.grn()

def int_to_binary(num, length=None):
    if length:
        return format(num, f'0{length}b')
    return format(num, 'b')

num1 = int(input("Vnesi n bitno stevilo: "))
num2 = int(input("Vnesi drugo m bitno stevilo: "))

max_length = max(len(int_to_binary(num1)), len(int_to_binary(num2)))
X = int_to_binary(num1, max_length)
A = int_to_binary(num2, max_length)

input_tuple = (0,) + tuple(int(bit)*100 for bit in X + A)
print(input_tuple)

lenX = len(X)
lenA = len(A)
lenOut = lenX + lenA

CSM.add_input_species("ZERO")

input_species = []

#Adding input species for A
for i in range(lenX):
    CSM.add_input_species("X"+str(i))
    input_species.append("X"+str(i))

#Adding input species for B
for i in range(lenA):
    CSM.add_input_species("Y"+str(i))
    input_species.append("Y"+str(i))

print(input_species)

out_indexes = []

#Prepare the first ands in the first row

for j in range(lenA):
    CSM.add_species("POA"+str(0)+str(j), 0.1)
    and_.and_("X0", "Y"+str(j), "POA"+str(0)+str(j), CSM)

out_indexes.append("POA"+str(0)+str(0))


for i in range(1, lenX+1):
    for j in range(lenA-1):
        if i < lenX:
            CSM.add_species("POA"+str(i)+str(j), 0.1)
            and_.and_("X"+str(i), "Y"+str(j), "POA"+str(i)+str(j), CSM)
        
        CSM.add_species("POFAS"+str(i)+str(j), 0.1)
        CSM.add_species("POFAC"+str(i)+str(j), 0.1)

        if i == 1: #In the first row the Cin is ZERO 
            full_adder.full_adder(str(i)+str(j), "POA"+str(i)+str(j), "POA"+str(i-1)+str(j+1), "ZERO", 
                                "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
            if j == 0: #Save the sum
                out_indexes.append("POFAS"+str(i)+str(j))
        
        elif i > 1 and i < lenX:
            if j == lenA-2: #If we are at the last bit of A in the row the Y is Aj+1 and Xi-1
                CSM.add_species("POA"+str(i-1)+str(j+1), 0.1)
                and_.and_("X"+str(i-1), "Y"+str(j+1), "POA"+str(i-1)+str(j+1), CSM)

                full_adder.full_adder(str(i)+str(j), "POA"+str(i)+str(j), "POA"+str(i-1)+str(j+1), "POFAC"+str(i-1)+str(j), 
                                    "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
            else:
                full_adder.full_adder(str(i)+str(j), "POA"+str(i)+str(j), "POFAS"+str(i-1)+str(j+1),
                                    "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                if j == 0: #Save the sum
                    out_indexes.append("POFAS"+str(i)+str(j))
        else: #I == lenX
            if j == 0: #X becomes ZERO
                full_adder.full_adder(str(i)+str(j), "ZERO", "POFAS"+str(i-1)+str(j+1),
                                    "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j)) #Save the sum

            elif j == lenA-2: #A becomes Aj+1 and X-1
                CSM.add_species("POA"+str(i-1)+str(j+1), 0.1)
                and_.and_("X"+str(i-1), "Y"+str(j+1), "POA"+str(i-1)+str(j+1), CSM)

                full_adder.full_adder(str(i)+str(j), "POFAC"+str(i)+str(j-1), "POA"+str(i-1)+str(j+1), 
                                    "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j)) #Save the sum
            else:
                full_adder.full_adder(str(i)+str(j), "POFAC"+str(i)+str(j-1), "POFAS"+str(i-1)+str(j+1), 
                                    "POFAC"+str(i-1)+str(j), "POFAS"+str(i)+str(j), "POFAC"+str(i)+str(j), CSM)
                out_indexes.append("POFAS"+str(i)+str(j))

T_FA, Y_FA = simulator.simulate_single(CSM, input_tuple, t_end=1000)

final_output = []
print(out_indexes)

for a in out_indexes:
    if Y_FA[:, CSM.species_names.index(a)][-1] > 50:
        final_output.append(str(1))
    else:
        final_output.append(str(0))
print("Binarni izhod:" ,"".join(final_output), "Decimalni izhod:", int("".join(final_output), 2) )



            