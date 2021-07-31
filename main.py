from src import (file_manager, plotting, syracuse)


def main():
    rng = range(1,10000)
    sequences = []
    for i in rng:
        sequence = syracuse.Syracuse(i)
        seq = sequence.run()
        sequences.append(seq)
        
    file_manager.dump(sequences)

    plotting.plot(sequences)
    


if __name__ == "__main__":
    main()