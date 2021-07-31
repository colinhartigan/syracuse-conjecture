import matplotlib.pyplot as plt
import numpy as np
import mplcursors

def plot(y_data):
    print("plotting...")
    for sequence in y_data:
        plt.plot(list(range(len(sequence))), sequence)

    plt.xlabel('iteration')
    plt.ylabel('value')

    plt.show()