#!/usr/bin/python3

status = True
tentativa = 0

while status:
    print('Exutando {}'.format(tentativa))
    
    tentativa += 1
    
    if tentativa == 10:
        status = False