from factory import factory

my_data         = factory.get_data_A()
my_mutation     = factory.get_mutation_A()
my_selector     = factory.get_selector_A()
my_constructive = factory.get_constructive_A()
my_reprodoction = factory.get_reproduction_A()

my_solver       = factory.get_solver_A()

my_solver.set_data(my_data)
my_solver.set_selector(my_selector)
my_solver.set_mutation(my_mutation)
my_solver.set_constructive(my_constructive)
my_solver.set_reproduction(my_reprodoction)

caminho_entrada = input("caminho do arquivo de entrada:")
caminho_saida   = input("caminho do arquivo de saida:")

my_data.read_Data(caminho_entrada)

my_solver.solve()

my_data.write_Data(caminho_saida)