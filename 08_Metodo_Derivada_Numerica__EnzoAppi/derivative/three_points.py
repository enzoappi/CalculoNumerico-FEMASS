from original import start_function
def derivada_TresPts(x):
  incremento = float(input('\nDigite o incremento: '))
  return(((-3 * start_function.func_orig(x)) + (4 * start_function.func_orig(x + incremento)) - (start_function.func_orig(x + 2 * incremento))) / (2 * incremento))
