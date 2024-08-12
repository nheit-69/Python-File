form = 'Register your form'
print(form)

name = str(input('Enter Your student Name'))
Class = input('Enter Your Class')
Age = int(input('Enter your age'))
print(name)
print(Class)
print(Age)

if Age>=18 and Age<=19:
    print('Older Teen')
elif Age<18:
    print('Young Teen')
elif Age>=20 and Age<=29:
    print('Young Adult')
elif Age>=30 and Age<=39:
    print('Thirties Adult')
elif Age>=40:
    print('Senior Adult')
