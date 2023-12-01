import numpy as np
import matplotlib.pyplot as plt
import juliet
import os

# This file is to download TESS data for WASP-18
tim, fl, fle = juliet.utils.get_all_TESS_data('WASP-18')

# For all data
for i in tim.keys():
    f1 = open(os.getcwd() + '/Data/WASP-18_' + str(i) + '.dat', 'w')
    for j in range(len(tim[i])):
        f1.write(str(tim[i][j]) + '\t' + str(fl[i][j]) + '\t' + str(fle[i][j]) + '\n')
    f1.close()

# For only eclipse data
for i in tim.keys():
    per, t0, t14 = 0.94145223, 2456740.80560, 2.21/24
    phs = juliet.utils.get_phases(tim[i], per, t0)
    mask = np.where(np.abs(phs*per) >= t14)[0]
    f1 = open(os.getcwd() + '/Data/WASP-18_only_eclipse_' + str(i) + '.dat', 'w')
    tim1, fl1, fle1 = tim[i][mask], fl[i][mask], fle[i][mask]
    for j in range(len(tim1)):
        f1.write(str(tim1[j]) + '\t' + str(fl1[j]) + '\t' + str(fle1[j]) + '\n')
    f1.close()