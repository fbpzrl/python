entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é {0}.'.format(type(entrada)))
print('Só tem espaços? {0}'.format(entrada.isspace()))
print('É um número? {0}'.format(entrada.isnumeric()))
print('É alfabético? {0}'.format(entrada.isalpha()))
print('Está em maiúsculas? {0}'.format(entrada.isupper()))
print('Está em minúsculas? {0}'.format(entrada.islower()))
print('Está capitalizada? {0}'.format(entrada.istitle()))