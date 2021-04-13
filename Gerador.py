import os
import time
import random , string

# Titulo do nosso cmd
os.system("cls")
os.system("title Gerador de Senha - Generator of Passwords")

print(""" 
   _____                    _              _____          _____            _           
  / ____|                  | |            |  __ \        / ____|          | |          
 | |  __  ___ _ __ __ _  __| | ___  _ __  | |  | | ___  | (___   ___ _ __ | |__   __ _ 
 | | |_ |/ _ \ '__/ _` |/ _` |/ _ \| '__| | |  | |/ _ \  \___ \ / _ \ '_ \| '_ \ / _` |
 | |__| |  __/ | | (_| | (_| | (_) | |    | |__| |  __/  ____) |  __/ | | | | | | (_| |
  \_____|\___|_|  \__,_|\__,_|\___/|_|    |_____/ \___| |_____/ \___|_| |_|_| |_|\__,_|
                                                                                       
                                                                                       
 """)

time.sleep(2)

amount = int(input('Quantas senhas você quer : '))
value = 1
while value <= amount:
    code = "" + ('').join(random.choices(string.ascii_letters + string.digits, k=5))
    f = open('Senhas.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'GERADO {code}')
    value += 1