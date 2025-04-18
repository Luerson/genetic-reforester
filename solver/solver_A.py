from .solver import solver

class solver_A(solver):
    
    def set_data(self, data):
        self.data = data
    
    def set_selector(self, selector):
        self.selector = selector
    
    def set_mutation(self, mutation):
        self.mutation = mutation
    
    def set_constructive(self, constructive):
        self.constructive = constructive
    
    def set_reproduction(self, reproduction):
        self.reproduction = reproduction
    
    def set_generation(self, generation):
        self.generation = generation

    def solve(self):
        return "resolvendo '-'"