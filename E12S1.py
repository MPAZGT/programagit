# adivinar el número #
import random

numRandom = random.randint(1,10)
intents = 0 
print('intenta adivinar el número con 3 intentos')

while intents < 3:
    print(f'Intentos {intents}')

    intent = int(input())
    intents += 1
    
    if intent < numRandom:
        print('tu intento es bajo')
    
    elif intent > numRandom:
        print('tu intento es mayor')
    else: 
        break
if intent == numRandom:
    print(f'adivinaste el número')
else: 
    print(f'lo siento, el número era {numRandom}')