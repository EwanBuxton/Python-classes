from random import *

characters = ["Jackie", "Martin", "Jim", "Adam", "Jonny"]
shuffle(characters)
sent = characters[0]
for char in characters[1:len(characters)-1]: sent+=f', {char}'
sent+= f' and {characters[-1]}.'
print (sent)


    
