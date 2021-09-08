class sqrt_rand:
    from math import sqrt
    
    def __init__(self, seed=0.01 , increment=1):
        self.original_seed = seed
        self.seed = seed
        self.increment = increment
        
    def rand(self, value=1, increase=True):
        x = self.sqrt(self.seed) 
        y = x - round(x)
        result = y * value * 2
 
        if increase:
            self.increase_seed()    
        
        return result
    
    def modify(self, result, positive=True, negative=True):
        if positive and negative == False and result < 0:
            result = -result
        elif negative and positive == False and result > 0:
            result = -result    
        return result
        
    def next_rand(self, value=1, positive=True, negative=True):
        self.randomize()
        return self.modify(self.rand(value), positive, negative)
    
    def randp(self, value=1):
       self.randomize()
       return self.modify(self.rand(value), True, False)
    
    def randn(self, value=1):
        self.randomize()
        return self.modify(self.rand(value), False, True)
        
    def increase_seed(self, increment=1):
        self.seed = self.seed + increment
        
    def rand_seed(self, value=1): 
        self.seed =  self.modify(self.rand(value), True, False)
        
    def randomize(self):
        self.rand_seed(self.increment)
