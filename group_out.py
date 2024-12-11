import simulator, grn
import numpy as np


def group_out(in1,in2,out,FA: grn.grn):

    #X_and AND Y_and  = OUT
    AandB = [{'name':in1, 'type': 1, 'Kd': 5, 'n': 2},
            {'name': in2, 'type': 1, 'Kd': 5, 'n': 3}]
    ResAandB = [{'name': out}]
    FA.add_gene(10, AandB, ResAandB,"or")