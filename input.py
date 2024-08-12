hello = '''Dear <Student> Your Presentation is on Osi model
 regard 
 google
 Email
 Time
 Date
 State
 Country'''
enter = input("Enter Student Name")
boss = input("Enter boss name")
em = input("Enter your Email")
ti = input("Enter your time")
da = input("Enter your Date")
st = input("Enter your state")
co = input("Enter your country")

hello = hello.replace("Student",enter)
hello = hello.replace("google",boss)
hello = hello.replace("Email",em)
hello = hello.replace("Time",ti)
hello = hello.replace("Date",da)
hello = hello.replace("State",st)
hello = hello.replace("Country",co)

print(hello)