from .selector import selector

class selector_A(selector):

    def select(self, population, forest):
        return "selecionando de " + str(population) + " com " + str(forest)