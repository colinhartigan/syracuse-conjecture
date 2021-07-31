class Syracuse:

    def __init__(self,seed):
        self.seed = seed 
        self.sequence = []
        self.current = self.seed

    def next(self):
        self.sequence.append(self.current)
        if self.current % 2 == 0:    
            self.current = self.current // 2 
        else:
            self.current = 3 * self.current + 1

    def run(self):
        #print(f"running simulation for {self.seed}")
        while self.sequence[-3:] != [4,2,1]:
            self.next()
        return self.sequence