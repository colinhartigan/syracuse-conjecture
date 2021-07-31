import os

cur_path = os.path.dirname(__file__)
seq_path = os.path.join(cur_path,"../data/sequences.txt")

def dump(sequences):
    with open(seq_path,"w") as f:
        f.write("\n".join(" ".join(str(j) for j in i) for i in sequences))

def load():
    with open(seq_path,"r") as f:
        lines = f.readlines()
        return [list(map(int,line.split())) for line in lines]