from original import start_function

def derivada_CincoPts(x):
  incremento = float(input('\nDigite o incremento: '))
  return(((start_function.func_orig(x - 2 * incremento)) - (8 * start_function.func_orig(x - incremento)) + (8 * start_function.func_orig(x + incremento)) - (start_function.func_orig(x + 2 * incremento))) / 12 * incremento)
