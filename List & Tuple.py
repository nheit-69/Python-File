# Sequences types
# 1. String 'hello world'
# 2. List ['hello', 87j, 84.9, "world"]  separate with comma (,)
# 3. Tuple ('hello', 84.5, 83, "game") or 'hello', 84.5, 83, "game"
#------------------------------------------------------------------------------------#
# using List[] ---> this symbol represent the list

kz = [67, 84, 1, 5, 8,4,'hello']
print(kz)
print(type(kz))
kz[1]= "name"   # use for replace the Data
print(kz)
kz[0]= "pip"
print(kz)
kz.sort()  # use for arrange the Data in sequence
print(kz)
kz.reverse()  # use for arrange the Data in Reverse
print(kz)
kz.append(999) # use for add something number or name
print(kz)
kz.append('word')
print(kz)
kz.insert(1,8894) # use for add something number or name
print(kz)
kz.insert(0,"hello python")
print(kz)
kz.insert(-3,9999)
print(kz)
king= kz.pop(3)  # used to remove and return the last element from a list.
print(king)
jhon = kz.pop(1)
print(jhon)
kz.remove(67)  # use for remove number or name
print(kz)
kz.remove('hello')
print(kz)


kz = ['game changer',"python", 8.39j]
print(kz)
print(type(kz))

print(kz[1])
print(kz[-1])

#---------------------------------------------------------------------------------------><

# using Tuple symbol--> ('hello', 84.5, 83, "game") or 'hello', 84.5, 83, "game"

kz = ('hello', "user", 84, 89.8, 94j)
print(kz)
print(type(kz))
print(kz[1])
print(kz[-1])
print(len(kz))


