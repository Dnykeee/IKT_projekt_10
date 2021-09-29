name=input('Hogy hívnak ? ')
age=int(input('Hány éves ? '))
kg=int(input('Hány kg vagy ? '))
cm=int(input('Hány cm vagy ? '))
print('Szia '+ name +', aki ',age,' éves',kg,'kg és',cm , 'cm magas')

if(cm <177):
    print('törpe geci')
if(age <15):
    print('noki')