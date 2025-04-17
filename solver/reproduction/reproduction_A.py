from .reproduction import reproduction

class reproduction_A(reproduction):

    def rep(self, curr_sol_1, curr_sol_2):
        return "reproduzindo com " + curr_sol_1 + " e " + curr_sol_2