from original import start_function

def derivada_simples(x):
  incremento = float(input('\nDigite o incremento: '))
  return((start_function.func_orig(x + incremento) - start_function.func_orig(x)) / incremento)
