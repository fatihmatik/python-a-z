import numpy as np
from numpy.random import randn
from time import time

if __name__ == "__main__":


    #### Expected value is 68.2
    N_list = []
    outer_count = 0 
    outer_obs = 100 # The outer loop count 
    while outer_count < outer_obs:

        observation = 100000 # the inner loop count
        count = 0
        N_quantity = 0
        number = None
        while count < observation:
            number = randn()
            if number > -1 and  number < 1:
                N_quantity += 1
            else: pass
            count += 1

        # Converting the quantity of observations that fall between the
        # 1st standard derivation to a percentage
        N_perc = "{:.2f}".format((N_quantity / observation) * 100)
        N_list.append(float(N_perc))

        outer_count +=1
    

    # Calculating the average percentage of all the percentages.
    total_perc = 0
    for perc in N_list:
        total_perc += perc
    total_perc = total_perc / outer_obs
    
    print(total_perc)

    
