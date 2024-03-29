a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print (a.difference(b))
set([1, 2])
print( b.difference(a))
set([5, 6])


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print (a.symmetric_difference(b))
set([1, 2, 5, 6])


planetas1 = {'Vênus', 'Mercúrio', 'Terra2', 'Netuno', 'Plutao'}
planetas2 = {'Júpiter', 'Terra', 'Urano', 'Saturno', 'Marte'}
print(planetas1 & planetas2)
print(planetas1.intersection(planetas2))