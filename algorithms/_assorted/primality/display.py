import brute_force as bf
import matplotlib.pyplot as plt
import miller_rabin as mr
import numpy as np
import time


data = {}

def add_data(label, fn, data_set, args="") -> float:
    df = np.empty(len(data_set))
    for i in range(len(data_set)):
        st = time.perf_counter_ns()
        fn(data_set[i])
        end = time.perf_counter_ns()
        df[i] = (end - st) * 1/1
    data[label] = df

if __name__ == "__main__":
    big_int = [2, 3, 5, 7, 9, 13, 17, 23, 29, 31, 47, 79, 166, 221, 1165, 1245, 6661, 91034, 12359, 178352, 21065]
    #big_int = [2, 3, 5, 7, 9, 13, 17, 23, 29, 31, 47, 51, 71, 161, 162] 
    #big_int = [15116, 15125, 96197, 21478]
    #big_int = [1451251]
    add_data("numb", bf.numb, big_int)
    #add_data("linear", bf.linear, big_int)
    #add_data("log", bf.log, big_int)
    #add_data("eliminatory", bf.eliminatory, big_int)
    add_data("miller_rabin", mr.is_prime, big_int, args="trys=1")

    print(data)
    print(big_int)
    plt.plot(data["numb"], big_int, "bo-")
    plt.plot(data["miller_rabin"], big_int, "ro-")
    plt.show()


