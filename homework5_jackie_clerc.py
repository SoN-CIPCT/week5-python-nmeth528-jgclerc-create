mylist=['item1','item2','item3','item4','item5','item6']
print(mylist)
message=f'The first two items in the list are:';
print(message,mylist[0:2])
message2=f'The middle two items in the list are:'
print(message2,mylist[2:4])
message3=f'The first and last items in the list are:'
print(message3,mylist[0], mylist[5])

menu=('pasta', 'curry', 'grilled cheese', 'brownie', 'cookie')
for meal in menu:
    print(menu)
menu=('pasta', 'curry', 'hamburger', 'brownie', 'flan')
print("\nModified menu:")
for meal in menu:
    print(menu)