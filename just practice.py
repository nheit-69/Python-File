# # k = 9
# # z = 69
# # kz = k+z
# # print(kz)
# # print(type(kz7))
#
#
# # name = "prem\n"
# # phone = "7042837433\n"
# # email = "prem838@gmail.com\n"
# # address = "147 Lodhi road new Delhi\n"
# # pincode = 110003
# #
# # form = (name+phone+email+address)
# # print(form)
# # # print(type(form))
#
#
# # chips = 4
# # juice = 7
# #
# # total = (chips + juice)
# # print(total)
#
# # name = "prem"
# # no = 1
# # subject = "Science = 45"
# # s1 = "Maths = 83"
# # s2 = "Hindi = 98"
# # s3 = "Physics = 90"
# # percent = 90.8
# #
# #
# # print(name)
# # print(no)
# # print(subject)
# # print(s1)
# # print(s2)
# # print(s3)
# # print(percent)
# #
# # print(type(name))       #string
# # print(type(no))         #integer
# # print(type(percent))    #floating
#
#
# # news = """Headline :- Yuvraj Singh enters Team India dressing room with folded hands, Rahul Dravid teases suspense
# # after India beat USA."""
# # Yuvraj = '''\nTeam India had a special guest visit them inside the dressing room, and it was none other than Yuvraj
# # Singh, one of India's greatest match-winners. Fewer people know about making an impact in, let alone one but two
# # World Cups. Who can forget his invaluable contributions in India's 2007 and 2011 World Cup campaigns? Be it the six
# # sixes off Stuart Broad in Johannesburg or scoring a fighting century against West Indies while battling cancer.
# # Whenever history talks about India's World Cup wins, Yuvraj's name would be taken before anyone else\n.'''
# #
# # News = news + Yuvraj
# # print(News)
# # print(Yuvraj[:])
# # print(Yuvraj[1:-15])
# # print(Yuvraj[3:90])
# # print(Yuvraj[90:])
# # print(Yuvraj[:])
# # print(Yuvraj[-9: ])
#
#
# # name= input("Enter Your Name")
# # Roll = int(input("Enter Your Roll.no"))
# # phone = int(input("Enter your Phone.no"))
# # percent= int(input("Enter your Percentage % "))
# # print(name)
# # print(type(name))
# # print(Roll)
# # print(phone)
# # print(percent)
#
#
# # fruits = ('apple','cherry','mango',8)     # tuple
# # print(fruits)
# # print(type(fruits))
# # student = input('Enter Student Name')
# # student = ['rohit', 'sandeep', 'mohal', 'ram', 'sohan', 'mohit', 'dikshant']      # List
# # print(student)
# # print(type(student))
# # print(student[1:-2])
# student = [8,3,5,3,62,62,2,6,25,62]
# # student[1] = 'jip'
# # student[1]= 'jeio'  #used for replace the data
# # print(student)
# student.reverse()  # used for reverse
# print(student)
# student.sort()  # used for arrange in sequence
# print(student)
# student.append(9999) # used for add
# print(student)
# student.insert(1,'minz')  # used for insert the data
# print(student)
# student.insert(3,'prem')
# print(student)
# student.sort()
# print(student)
# student = student.pop[3]
# print(student)
# student.remove(3)
# print(student)



# windows = {"created" : "1985",
#            "owner" : "billgates",
#            "billgates" : "Microsoft",
#            "Networth" : "$9999 billion"}
# print(windows)
# print(windows["owner"])
# print(windows["billgates"])
# print(windows.keys())
# print(windows.values())
# print(windows.items())

#set

# India = {"Delhi" , "Mumbai" , "Uttar Pradesh", "Uttarakhand", "Jharkhand"}
# # print(India)
# # print(type(India))
# India.add('Madhya Pradesh')
# print(India)
# India.remove('Mumbai')
# print(India)
# # India.clear()
# # print(India)
# print('Asia No.1 City' , India)



# number = {8, 2, 5, 24, 3,9, 8.9, 1.1,'The'}
# print(number)
# number.add(-84)
# print(number)
# number.remove(1.1)
# print(number)
# number.clear()
# print(number)
# number.copy()
# print(number)
# number2 = number.copy()
# print(number)
# print ('number' , number)
# number2 = number.remove(8)
# print('number2', number)

# integer = {1, 4, 5, 6, 45, 96, 100, 895, 94, "hello"}    #  using discard()
# print(integer)
# integer.discard(45)
# print(integer)
# integer.discard('hello')
# print(integer)
# integer.discard(83.4)
# print(integer)


# mobile = {1,2,3,4}        #using intersection()
# mobile2 = {4,3,2,1}
# print(mobile.intersection(mobile2))

# roadnum = {20,30,40,50,60,70,80,90,100}
# roadnum2 = {83,20,50,93,80,39,90,90,10,}
# print(roadnum.intersection(roadnum2))

# fruit_basket = {'apple','banana','orange', 'strawberry', 'blackberry', 'watermelon'}
# fruit2_basket = {'peas', 'mango', 'orange', 'guava', 'banana', 'apple'}
# fruit3_basket = {'mango', 'orange', 'watermelon', 'berry',}
#
# print(fruit.intersection(fruit2))
# print(fruit.intersection(fruit3))
# print(fruit3.intersection(fruit))
# print(fruit2.intersection(fruit))
# print(fruit.intersection(fruit2, fruit3))
# print(fruit3.intersection(fruit, fruit2))
# print('same fruit & fruit2 on basket: ', fruit_basket.intersection(fruit2_basket))
# print('same fruit2 & 3 on basket :',fruit2_basket.intersection(fruit3_basket))
# print('same fruit & 2,3 :', fruit_basket.intersection(fruit2_basket , fruit3_basket))






# print(fruit.symmetric_difference(fruit2))         # using symmetric it is opposite to intersection
# print(fruit3.symmetric_difference(fruit))
# print(fruit2.symmetric_difference(fruit))
# print('fruit & 2 on basket', (fruit_basket.symmetric_difference(fruit2_basket)))


# Conditional statement

# a = 60                    # using if statement
# if 23 > 20 :
#     print("23 greater than a")
# if 19 < 20 :
#     print("19 smaller than a")
# if 50 > 20:
#     print("50 greater than 20")



# Tshirt = 300
# jeans = 300
#
# if Tshirt > jeans :
#     print("Tshirt more expensive than jeans")
# elif Tshirt < jeans :
#     print("Tshirt less expensive than jeans")
# elif Tshirt == jeans :
#     print("Tshirt and jeans same price")
# else :
#     print("Price invalid")

                                                                        # if elif else statement
# try:
#     marks = float(input("Enter your Marks percentage\nOut of 100 : - "))
#
#     if marks > 90 :
#         print("1st Division")
#     elif marks == 90 :
#         print("1st Division")
#     elif marks > 80 :
#         print("2nd Division")
#     elif marks == 80 :
#         print("2nd Division")
#     elif marks > 65 :
#         print("3rd Division")
#     elif marks == 65 :
#         print("3rd Division")
#     elif marks > 45 :
#         print("You are pass")
#     elif marks == 45 :
#         print("You are pass")
#     elif marks < 45:
#         print("You are fail")
#     else:
#         print("Invalid Input")
# except ValueError:
#     print("Invalid Input: please type numeric value")


   # loops while, for loops
# tshirt = 70
# jeans = 85
#
# while jeans > tshirt :
#     print("jeans is greater than tshirt")
#     tshirt = tshirt + 1
#     print(str(tshirt))



# apple = 10
#
# while 30 > apple :
#     print("is greater than apple")
#     apple = apple + 1
#     print(str(apple))


# for fruit in range (30) :            # using break statement
#     if fruit == 15:
#         break
#     print(str(fruit ))
#     print(type(fruit))
#     print(fruit + 2)


# for cherry in range (20) :             # using continue statement
#     if cherry == 15 :
#         continue
#     print('cherry')
#     print(cherry)

# for hello in range (1, 10,2) :
#     # print(hello)
#     hello = hello + 1
#     print(hello)
#     if hello == 10:
#         print('complete')
#     # else :
#     #     print('nothing')


# T568_A = ['Green White', 'Green', 'Orange White', 'Blue', 'Blue White', 'Orange', 'Brown White', 'Brown']
# color = 0
# for color in  T568_A :
#     print(T568_A[4])


# T568_B = ['Orange White', "Orange", 'Green White', 'Blue', 'Blue White', 'Green', 'Brown White', 'Brown']
# color = 0
# for color in T568_B :
#     print(T568_B[2])


# coin = ['Gold', 'Silver', 'Purple', 'Yellow', 'Black']
# color_coin = 0
# # for color_coin in coin:
# #     print(coin[1])



# qrcode         install three Module:- qrcode, image, jpg-png

# import qrcode
# img = qrcode.make('youtube.com')
# img.save('youtube.png')


