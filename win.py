import random
import os
maps = ['World of Tomorrow', 'Club 27', 'Freedom Fighters', 'Situs Inversus', 'Hokkaido', 'Nightcall', 'The Finish Line', 'A Silver Tongue', 'Another Life' ,'A Better Pill', 'The Ark Society', 'Golden Handshake', 'The Last Resort', 'On Top of the World', 'Death in the Family', 'Apex Predator', 'End of an Era', 'The Farewell', 'The Last Yardbird', 'The Pen and the Sword', 'Crime and Punishment']

a = 1
while a == 1:
    os.system('cls')
    print(random.choice(maps))
    print("")
    input()
