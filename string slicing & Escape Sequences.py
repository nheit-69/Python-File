# jai[start:stop]   items start through stop-1
# jai[start:]       items start through the rest of the array
# jai[:stop]        items from the beginning through stop-1
# jai[:]            a copy of the whole array
# jai[start:stop:step]  start through not past stop, by step
#--------------------------------------><

# Escape sequences  (\)-->>backslash-----represent whitespace means tab,space.
# \n -->> means new line
# \t -->> means tab space between character


kz = '''is just the fifth Indian bowler (third spinner)
 after Kapil Dev, Anil Kumble,\n Harbhajan\t Singh, and Ishant Sharma
  to achieve the feat. In fact, the off-spinner is only the sixth spinner
   in Test cricket's rich history \nto complete the milestone after Muttiah 
   Muralitharan, Shane Warne, Anil Kumble, \tNathan Lyon, and Harbhajan Singh.'''

print(kz)
print(type(kz))
print(kz[ : ])
print(kz[3:8])
print(kz[:67])
print(kz[9:100:4])
print(kz[:])
print(kz[:11])
print(kz[9:])
print(kz[:-99])
print(kz[-189:])
# ---------------------------------------><
# Using len()
print(len(kz))  #used for length how many character are there
# -------------------------------------------------------------------><
# Using .endswith() and .startswith()
print(kz.endswith("Singh."))  #for true/false
print(kz.startswith("is"))    #for true/false
# -------------------------------------------------------------><
# using .find()
print(kz.find("Lyon"))  # used for find keyword
# -----------------------------------------------------------------><
# using .replace
#  Type Like this print(kz.replace("Lyon", "John"))
print(kz.replace("John", "Lyon")) # used for replace the character


# practice _______________________________________________________
print(kz.replace("Dev", "hello"))
print(len(kz))
print(kz.startswith("hi"))
print(kz.endswith("game"))
print(len("hello"))
print(len("Lyon"))
print(kz.replace("hello", "where"))
print(kz.find("where"))
