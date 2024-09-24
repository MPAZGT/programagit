#verificar un palindromo#
palabra=input('Dime una palabra: ').lower()
if palabra==palabra[::-1]:
  print('Es un Palíndromo')
else:
  print('No es un Palíndromo')