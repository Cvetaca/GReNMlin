import full_adder
import half_adder
import and_
import grn
AM=grn.grn()
#full_adder.full_adder(1,test)

lenA=4
lenB=4
lenOut=lenA+lenB

AM.add_input_species("ZERO")

for i in range(lenA):
    AM.add_input_species("A"+str(i))
for i in range(lenB):
    AM.add_input_species("B"+str(i))
for i in range(lenOut):
    AM.add_species("OUT"+str(i), 0.1)
i=0
for j in range(lenA):
    and_.and_("A"+str(j),"B0","PO"+i,AM)
    i+=1

