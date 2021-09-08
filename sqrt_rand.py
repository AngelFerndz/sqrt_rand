class sqrt_rand:
    from math import sqrt
    
    def __init__(self, seed=0.01 , increment=1):
        self.original_seed = seed
        self.seed = seed
        self.increment = increment
        
    def rand(self, value=1, positive=True, negative=True, increase=True):
        x = self.sqrt(self.seed) 
        y = x - round(x)
        result = y * value * 2
        
        if increase:
            self.increase_increment()
        
        if positive and negative == False and result < 0:
            result = -result
        elif negative and positive == False and result > 0:
            result = -result
        return result
    
    def randp(self, value=1, increase=True):
        return self.rand(value, positive=True, negative=False, increase=increase)
    
    def randn(self, value=1, increase=True):
        return self.rand(value, positive=False, negative=True, increase=increase)
        
    def increase_increment(self, increment=1):
        self.seed = self.seed + increment
        
    def rand_increment(self, value=1):
        self.increment = self.rand(value)
        
    def rand_seed(self, value=1):
        self.seed = self.randp(value)
        
