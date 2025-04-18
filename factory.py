from data.data_A import data_A
from solver.solver_A import solver_A
from solver.mutation.mutation_A import mutation_A
from solver.selector.selector_A import selector_A
from solver.solution.generation_A import generation_A
from solver.constructive.constructive_A import constructive_A
from solver.reproduction.reproduction_A import reproduction_A

class factory():

    @staticmethod
    def get_data_A():
        return data_A()
    
    @staticmethod
    def get_constructive_A():
        return constructive_A()

    @staticmethod
    def get_mutation_A():
        return mutation_A()

    @staticmethod
    def get_reproduction_A():
        return reproduction_A()
    
    @staticmethod
    def get_selector_A():
        return selector_A()
    
    @staticmethod
    def get_solver_A():
        return solver_A()
    
    @staticmethod    
    def get_generation_A():
        return generation_A()

    
    
