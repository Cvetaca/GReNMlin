import numpy as np 

def solve_model(T,state):
    ZERO, A4, A3, A2, A1, A0, B2, B1, B0, POFAS00, POFAS01, POFAS02, POFAS03, POFAS04, POA10, POFAS10, POFAC10, O110, O210, O310, POA11, POFAS11, POFAC11, O111, O211, O311, POA12, POFAS12, POFAC12, O112, O212, O312, POA13, POFAS13, POFAC13, O113, O213, O313, POA14, POFAS14, POFAC14, O114, O214, O314, POA20, POFAS20, POFAC20, O120, O220, O320, POA21, POFAS21, POFAC21, O121, O221, O321, POA22, POFAS22, POFAC22, O122, O222, O322, POA23, POFAS23, POFAC23, O123, O223, O323, POA24, POFAS24, POFAC24, O124, O224, O324 = state
    dZERO = -ZERO*0
    dA4 = -A4*0
    dA3 = -A3*0
    dA2 = -A2*0
    dA1 = -A1*0
    dA0 = -A0*0
    dB2 = -B2*0
    dB1 = -B1*0
    dB0 = -B0*0
    dPOFAS00 = -POFAS00*0.1+10*(((A0/5)**2)*((B0/5)**2))/(1+((A0/5)**2)+((B0/5)**2)+((A0/5)**2)*((B0/5)**2))
    dPOFAS01 = -POFAS01*0.1+10*(((A1/5)**2)*((B0/5)**2))/(1+((A1/5)**2)+((B0/5)**2)+((A1/5)**2)*((B0/5)**2))
    dPOFAS02 = -POFAS02*0.1+10*(((A2/5)**2)*((B0/5)**2))/(1+((A2/5)**2)+((B0/5)**2)+((A2/5)**2)*((B0/5)**2))
    dPOFAS03 = -POFAS03*0.1+10*(((A3/5)**2)*((B0/5)**2))/(1+((A3/5)**2)+((B0/5)**2)+((A3/5)**2)*((B0/5)**2))
    dPOFAS04 = -POFAS04*0.1+10*(((A4/5)**2)*((B0/5)**2))/(1+((A4/5)**2)+((B0/5)**2)+((A4/5)**2)*((B0/5)**2))
    dPOA10 = -POA10*0.1+10*(((A0/5)**2)*((B1/5)**2))/(1+((A0/5)**2)+((B1/5)**2)+((A0/5)**2)*((B1/5)**2))
    dPOFAS10 = -POFAS10*0.1+10*(((ZERO/5)**3))/(1+((O110/5)**2)+((ZERO/5)**3)+((O110/5)**2)*((ZERO/5)**3))+10*(((O110/5)**2))/(1+((O110/5)**2)+((ZERO/5)**3)+((O110/5)**2)*((ZERO/5)**3))
    dPOFAC10 = -POFAC10*0.1+10*(((O210/5)**2)+((O310/5)**3)+((O210/5)**2)*((O310/5)**3))/(1+((O210/5)**2)+((O310/5)**3)+((O210/5)**2)*((O310/5)**3))
    dO110 = -O110*0.1+10*(((POA10/5)**3))/(1+((POFAS01/5)**2)+((POA10/5)**3)+((POFAS01/5)**2)*((POA10/5)**3))+10*(((POFAS01/5)**2))/(1+((POFAS01/5)**2)+((POA10/5)**3)+((POFAS01/5)**2)*((POA10/5)**3))
    dO210 = -O210*0.1+10*(((O110/5)**2)*((ZERO/5)**3))/(1+((O110/5)**2)+((ZERO/5)**3)+((O110/5)**2)*((ZERO/5)**3))
    dO310 = -O310*0.1+10*(((POFAS01/5)**2)*((POA10/5)**3))/(1+((POFAS01/5)**2)+((POA10/5)**3)+((POFAS01/5)**2)*((POA10/5)**3))
    dPOA11 = -POA11*0.1+10*(((A1/5)**2)*((B1/5)**2))/(1+((A1/5)**2)+((B1/5)**2)+((A1/5)**2)*((B1/5)**2))
    dPOFAS11 = -POFAS11*0.1+10*(((POFAC10/5)**3))/(1+((O111/5)**2)+((POFAC10/5)**3)+((O111/5)**2)*((POFAC10/5)**3))+10*(((O111/5)**2))/(1+((O111/5)**2)+((POFAC10/5)**3)+((O111/5)**2)*((POFAC10/5)**3))
    dPOFAC11 = -POFAC11*0.1+10*(((O211/5)**2)+((O311/5)**3)+((O211/5)**2)*((O311/5)**3))/(1+((O211/5)**2)+((O311/5)**3)+((O211/5)**2)*((O311/5)**3))
    dO111 = -O111*0.1+10*(((POA11/5)**3))/(1+((POFAS02/5)**2)+((POA11/5)**3)+((POFAS02/5)**2)*((POA11/5)**3))+10*(((POFAS02/5)**2))/(1+((POFAS02/5)**2)+((POA11/5)**3)+((POFAS02/5)**2)*((POA11/5)**3))
    dO211 = -O211*0.1+10*(((O111/5)**2)*((POFAC10/5)**3))/(1+((O111/5)**2)+((POFAC10/5)**3)+((O111/5)**2)*((POFAC10/5)**3))
    dO311 = -O311*0.1+10*(((POFAS02/5)**2)*((POA11/5)**3))/(1+((POFAS02/5)**2)+((POA11/5)**3)+((POFAS02/5)**2)*((POA11/5)**3))
    dPOA12 = -POA12*0.1+10*(((A2/5)**2)*((B1/5)**2))/(1+((A2/5)**2)+((B1/5)**2)+((A2/5)**2)*((B1/5)**2))
    dPOFAS12 = -POFAS12*0.1+10*(((POFAC11/5)**3))/(1+((O112/5)**2)+((POFAC11/5)**3)+((O112/5)**2)*((POFAC11/5)**3))+10*(((O112/5)**2))/(1+((O112/5)**2)+((POFAC11/5)**3)+((O112/5)**2)*((POFAC11/5)**3))
    dPOFAC12 = -POFAC12*0.1+10*(((O212/5)**2)+((O312/5)**3)+((O212/5)**2)*((O312/5)**3))/(1+((O212/5)**2)+((O312/5)**3)+((O212/5)**2)*((O312/5)**3))
    dO112 = -O112*0.1+10*(((POA12/5)**3))/(1+((POFAS03/5)**2)+((POA12/5)**3)+((POFAS03/5)**2)*((POA12/5)**3))+10*(((POFAS03/5)**2))/(1+((POFAS03/5)**2)+((POA12/5)**3)+((POFAS03/5)**2)*((POA12/5)**3))
    dO212 = -O212*0.1+10*(((O112/5)**2)*((POFAC11/5)**3))/(1+((O112/5)**2)+((POFAC11/5)**3)+((O112/5)**2)*((POFAC11/5)**3))
    dO312 = -O312*0.1+10*(((POFAS03/5)**2)*((POA12/5)**3))/(1+((POFAS03/5)**2)+((POA12/5)**3)+((POFAS03/5)**2)*((POA12/5)**3))
    dPOA13 = -POA13*0.1+10*(((A3/5)**2)*((B1/5)**2))/(1+((A3/5)**2)+((B1/5)**2)+((A3/5)**2)*((B1/5)**2))
    dPOFAS13 = -POFAS13*0.1+10*(((POFAC12/5)**3))/(1+((O113/5)**2)+((POFAC12/5)**3)+((O113/5)**2)*((POFAC12/5)**3))+10*(((O113/5)**2))/(1+((O113/5)**2)+((POFAC12/5)**3)+((O113/5)**2)*((POFAC12/5)**3))
    dPOFAC13 = -POFAC13*0.1+10*(((O213/5)**2)+((O313/5)**3)+((O213/5)**2)*((O313/5)**3))/(1+((O213/5)**2)+((O313/5)**3)+((O213/5)**2)*((O313/5)**3))
    dO113 = -O113*0.1+10*(((POA13/5)**3))/(1+((POFAS04/5)**2)+((POA13/5)**3)+((POFAS04/5)**2)*((POA13/5)**3))+10*(((POFAS04/5)**2))/(1+((POFAS04/5)**2)+((POA13/5)**3)+((POFAS04/5)**2)*((POA13/5)**3))
    dO213 = -O213*0.1+10*(((O113/5)**2)*((POFAC12/5)**3))/(1+((O113/5)**2)+((POFAC12/5)**3)+((O113/5)**2)*((POFAC12/5)**3))
    dO313 = -O313*0.1+10*(((POFAS04/5)**2)*((POA13/5)**3))/(1+((POFAS04/5)**2)+((POA13/5)**3)+((POFAS04/5)**2)*((POA13/5)**3))
    dPOA14 = -POA14*0.1+10*(((A4/5)**2)*((B1/5)**2))/(1+((A4/5)**2)+((B1/5)**2)+((A4/5)**2)*((B1/5)**2))
    dPOFAS14 = -POFAS14*0.1+10*(((POFAC13/5)**3))/(1+((O114/5)**2)+((POFAC13/5)**3)+((O114/5)**2)*((POFAC13/5)**3))+10*(((O114/5)**2))/(1+((O114/5)**2)+((POFAC13/5)**3)+((O114/5)**2)*((POFAC13/5)**3))
    dPOFAC14 = -POFAC14*0.1+10*(((O214/5)**2)+((O314/5)**3)+((O214/5)**2)*((O314/5)**3))/(1+((O214/5)**2)+((O314/5)**3)+((O214/5)**2)*((O314/5)**3))
    dO114 = -O114*0.1+10*(((POA14/5)**3))/(1+((ZERO/5)**2)+((POA14/5)**3)+((ZERO/5)**2)*((POA14/5)**3))+10*(((ZERO/5)**2))/(1+((ZERO/5)**2)+((POA14/5)**3)+((ZERO/5)**2)*((POA14/5)**3))
    dO214 = -O214*0.1+10*(((O114/5)**2)*((POFAC13/5)**3))/(1+((O114/5)**2)+((POFAC13/5)**3)+((O114/5)**2)*((POFAC13/5)**3))
    dO314 = -O314*0.1+10*(((ZERO/5)**2)*((POA14/5)**3))/(1+((ZERO/5)**2)+((POA14/5)**3)+((ZERO/5)**2)*((POA14/5)**3))
    dPOA20 = -POA20*0.1+10*(((A0/5)**2)*((B2/5)**2))/(1+((A0/5)**2)+((B2/5)**2)+((A0/5)**2)*((B2/5)**2))
    dPOFAS20 = -POFAS20*0.1+10*(((ZERO/5)**3))/(1+((O120/5)**2)+((ZERO/5)**3)+((O120/5)**2)*((ZERO/5)**3))+10*(((O120/5)**2))/(1+((O120/5)**2)+((ZERO/5)**3)+((O120/5)**2)*((ZERO/5)**3))
    dPOFAC20 = -POFAC20*0.1+10*(((O220/5)**2)+((O320/5)**3)+((O220/5)**2)*((O320/5)**3))/(1+((O220/5)**2)+((O320/5)**3)+((O220/5)**2)*((O320/5)**3))
    dO120 = -O120*0.1+10*(((POA20/5)**3))/(1+((POFAS11/5)**2)+((POA20/5)**3)+((POFAS11/5)**2)*((POA20/5)**3))+10*(((POFAS11/5)**2))/(1+((POFAS11/5)**2)+((POA20/5)**3)+((POFAS11/5)**2)*((POA20/5)**3))
    dO220 = -O220*0.1+10*(((O120/5)**2)*((ZERO/5)**3))/(1+((O120/5)**2)+((ZERO/5)**3)+((O120/5)**2)*((ZERO/5)**3))
    dO320 = -O320*0.1+10*(((POFAS11/5)**2)*((POA20/5)**3))/(1+((POFAS11/5)**2)+((POA20/5)**3)+((POFAS11/5)**2)*((POA20/5)**3))
    dPOA21 = -POA21*0.1+10*(((A1/5)**2)*((B2/5)**2))/(1+((A1/5)**2)+((B2/5)**2)+((A1/5)**2)*((B2/5)**2))
    dPOFAS21 = -POFAS21*0.1+10*(((POFAC20/5)**3))/(1+((O121/5)**2)+((POFAC20/5)**3)+((O121/5)**2)*((POFAC20/5)**3))+10*(((O121/5)**2))/(1+((O121/5)**2)+((POFAC20/5)**3)+((O121/5)**2)*((POFAC20/5)**3))
    dPOFAC21 = -POFAC21*0.1+10*(((O221/5)**2)+((O321/5)**3)+((O221/5)**2)*((O321/5)**3))/(1+((O221/5)**2)+((O321/5)**3)+((O221/5)**2)*((O321/5)**3))
    dO121 = -O121*0.1+10*(((POA21/5)**3))/(1+((POFAS12/5)**2)+((POA21/5)**3)+((POFAS12/5)**2)*((POA21/5)**3))+10*(((POFAS12/5)**2))/(1+((POFAS12/5)**2)+((POA21/5)**3)+((POFAS12/5)**2)*((POA21/5)**3))
    dO221 = -O221*0.1+10*(((O121/5)**2)*((POFAC20/5)**3))/(1+((O121/5)**2)+((POFAC20/5)**3)+((O121/5)**2)*((POFAC20/5)**3))
    dO321 = -O321*0.1+10*(((POFAS12/5)**2)*((POA21/5)**3))/(1+((POFAS12/5)**2)+((POA21/5)**3)+((POFAS12/5)**2)*((POA21/5)**3))
    dPOA22 = -POA22*0.1+10*(((A2/5)**2)*((B2/5)**2))/(1+((A2/5)**2)+((B2/5)**2)+((A2/5)**2)*((B2/5)**2))
    dPOFAS22 = -POFAS22*0.1+10*(((POFAC21/5)**3))/(1+((O122/5)**2)+((POFAC21/5)**3)+((O122/5)**2)*((POFAC21/5)**3))+10*(((O122/5)**2))/(1+((O122/5)**2)+((POFAC21/5)**3)+((O122/5)**2)*((POFAC21/5)**3))
    dPOFAC22 = -POFAC22*0.1+10*(((O222/5)**2)+((O322/5)**3)+((O222/5)**2)*((O322/5)**3))/(1+((O222/5)**2)+((O322/5)**3)+((O222/5)**2)*((O322/5)**3))
    dO122 = -O122*0.1+10*(((POA22/5)**3))/(1+((POFAS13/5)**2)+((POA22/5)**3)+((POFAS13/5)**2)*((POA22/5)**3))+10*(((POFAS13/5)**2))/(1+((POFAS13/5)**2)+((POA22/5)**3)+((POFAS13/5)**2)*((POA22/5)**3))
    dO222 = -O222*0.1+10*(((O122/5)**2)*((POFAC21/5)**3))/(1+((O122/5)**2)+((POFAC21/5)**3)+((O122/5)**2)*((POFAC21/5)**3))
    dO322 = -O322*0.1+10*(((POFAS13/5)**2)*((POA22/5)**3))/(1+((POFAS13/5)**2)+((POA22/5)**3)+((POFAS13/5)**2)*((POA22/5)**3))
    dPOA23 = -POA23*0.1+10*(((A3/5)**2)*((B2/5)**2))/(1+((A3/5)**2)+((B2/5)**2)+((A3/5)**2)*((B2/5)**2))
    dPOFAS23 = -POFAS23*0.1+10*(((POFAC22/5)**3))/(1+((O123/5)**2)+((POFAC22/5)**3)+((O123/5)**2)*((POFAC22/5)**3))+10*(((O123/5)**2))/(1+((O123/5)**2)+((POFAC22/5)**3)+((O123/5)**2)*((POFAC22/5)**3))
    dPOFAC23 = -POFAC23*0.1+10*(((O223/5)**2)+((O323/5)**3)+((O223/5)**2)*((O323/5)**3))/(1+((O223/5)**2)+((O323/5)**3)+((O223/5)**2)*((O323/5)**3))
    dO123 = -O123*0.1+10*(((POA23/5)**3))/(1+((POFAS14/5)**2)+((POA23/5)**3)+((POFAS14/5)**2)*((POA23/5)**3))+10*(((POFAS14/5)**2))/(1+((POFAS14/5)**2)+((POA23/5)**3)+((POFAS14/5)**2)*((POA23/5)**3))
    dO223 = -O223*0.1+10*(((O123/5)**2)*((POFAC22/5)**3))/(1+((O123/5)**2)+((POFAC22/5)**3)+((O123/5)**2)*((POFAC22/5)**3))
    dO323 = -O323*0.1+10*(((POFAS14/5)**2)*((POA23/5)**3))/(1+((POFAS14/5)**2)+((POA23/5)**3)+((POFAS14/5)**2)*((POA23/5)**3))
    dPOA24 = -POA24*0.1+10*(((A4/5)**2)*((B2/5)**2))/(1+((A4/5)**2)+((B2/5)**2)+((A4/5)**2)*((B2/5)**2))
    dPOFAS24 = -POFAS24*0.1+10*(((POFAC23/5)**3))/(1+((O124/5)**2)+((POFAC23/5)**3)+((O124/5)**2)*((POFAC23/5)**3))+10*(((O124/5)**2))/(1+((O124/5)**2)+((POFAC23/5)**3)+((O124/5)**2)*((POFAC23/5)**3))
    dPOFAC24 = -POFAC24*0.1+10*(((O224/5)**2)+((O324/5)**3)+((O224/5)**2)*((O324/5)**3))/(1+((O224/5)**2)+((O324/5)**3)+((O224/5)**2)*((O324/5)**3))
    dO124 = -O124*0.1+10*(((POA24/5)**3))/(1+((POFAC14/5)**2)+((POA24/5)**3)+((POFAC14/5)**2)*((POA24/5)**3))+10*(((POFAC14/5)**2))/(1+((POFAC14/5)**2)+((POA24/5)**3)+((POFAC14/5)**2)*((POA24/5)**3))
    dO224 = -O224*0.1+10*(((O124/5)**2)*((POFAC23/5)**3))/(1+((O124/5)**2)+((POFAC23/5)**3)+((O124/5)**2)*((POFAC23/5)**3))
    dO324 = -O324*0.1+10*(((POFAC14/5)**2)*((POA24/5)**3))/(1+((POFAC14/5)**2)+((POA24/5)**3)+((POFAC14/5)**2)*((POA24/5)**3))
    return np.array([dZERO, dA4, dA3, dA2, dA1, dA0, dB2, dB1, dB0, dPOFAS00, dPOFAS01, dPOFAS02, dPOFAS03, dPOFAS04, dPOA10, dPOFAS10, dPOFAC10, dO110, dO210, dO310, dPOA11, dPOFAS11, dPOFAC11, dO111, dO211, dO311, dPOA12, dPOFAS12, dPOFAC12, dO112, dO212, dO312, dPOA13, dPOFAS13, dPOFAC13, dO113, dO213, dO313, dPOA14, dPOFAS14, dPOFAC14, dO114, dO214, dO314, dPOA20, dPOFAS20, dPOFAC20, dO120, dO220, dO320, dPOA21, dPOFAS21, dPOFAC21, dO121, dO221, dO321, dPOA22, dPOFAS22, dPOFAC22, dO122, dO222, dO322, dPOA23, dPOFAS23, dPOFAC23, dO123, dO223, dO323, dPOA24, dPOFAS24, dPOFAC24, dO124, dO224, dO324])

def solve_model_steady(state):
    return solve_model(0, state)
