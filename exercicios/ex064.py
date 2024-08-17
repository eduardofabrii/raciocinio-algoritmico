global var_global
var_global = 1
def funcao(var_global):
    var_local = 2
    print(var_global)
    print(var_local)

    # Recebe parametro e
    #  roda a funcao que pintra 3,
    #  (da primeira variavel var global
    #  e depois printa var local)
funcao(3)
# Printa o que está na var
#  global pq a funcao deixou de existir
print(var_global)



