from .solver import solver
import random

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
    
    def set_adaptation(self, adaptation):
        self.adaptation = adaptation

    def solve(self):
        solutions = self.constructive.construct_init(self.data.mapa_binario_restauravel)

        for i in range(20):
            solutions = self.selector.select(solutions, self.data.mapa_binario_floresta)
            offspring = self.reproduction.reproduction_init(solutions, self.data.mapa_binario_restauravel)

            for i in range(len(offspring)):
                offspring[i] = self.adaptation.mut(offspring[i], self.data.mapa_binario_floresta, self.data.mapa_binario_restauravel)
                if random.random() < 0.1:
                    print("MUTAÇÃO")
                    offspring[i] = self.mutation.mut(offspring[i], self.data.mapa_binario_floresta, self.data.mapa_binario_restauravel)
            
            solutions += offspring
        
        while len(solutions) > 12:
            solutions = self.selector.select(solutions, self.data.mapa_binario_floresta)
        
        return solutions