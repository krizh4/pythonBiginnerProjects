import os

adj0 = input('Adjective 0: ')
adj1 = input('Adjective 1: ')
bird = input('Type of bird: ')
room = input('Room in a house: ')
vrb0 = input('Verb (past tense): ')
vrb1 = input('Verb: ')
vrb2 = input('Verb ending with ing: ')
vrb3 = input('Another Verb ending with ing: ')
rnme = input('Relative\'s name: ' )
nun0 = input('Noun: ')
nun1 = input('Plural noun: ')
nun2 = input('Noun: ')
liqd = input('A liquid: ')
prtb = input('part of the body (plural): ')

print('\n __________________________________________ \n')

print(f"It was a {adj0}, cold November day. I woke up to the {adj1} smell of {bird} roasting in the \
{room} downstairs. I {vrb0} down the stairs to see if I could help {vrb1} dinner. \
My mom said, \"see if {rnme} needs a fresh {nun0}.\" So I carried a tray of glasses \
full of {liqd} into the {vrb2} room. When I got there, I couldn't believe my {prtb}! \
There were {nun1} {vrb3} on the {nun2}")

print('\n __________________________________________ \n')

os.system('pause')