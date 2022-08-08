import json
import os
import re

def file(filename):
    if not os.path.exists(filename):
        a=open(filename,"w+")
        a.write("[]")
def read_data(filename):
    b=open(filename,"r")
    c=json.loads(b.read())
    return c
def signup(filename):
    k=input(".....welcome to  signup page")
    user=input("enter the name:>")
    if user=="a" or "A" and user=="z" or "Z":
        password=input("enter the password:>")
    if not(re.search("[a-z A-Z]",password) and re.search('[0-9]',password) and re.search('[@#$]',password)):
        print("invalid password:>")
        return""
    conf_pass=input("confirm your password:>")
    if password!=conf_pass:
        print("password did not match")
        return " "
    contact=input("enter the contact:>")
    if len(contact)==10:
        gender=input("enter your gender")
        if gender=="male" or gender=="female":
            age=int(input("enter your age"))
            if age>18 and age<50:
                print("you can signup")
                dob=(input("enter your dob"))
        email=input("enter the email")
        json_data=read_data(filename)
        for u in json_data:
            if u ["name"]==user:
                print("use already exist")
                return " "
        json_data.append({"name":user,"password":password,"contant":contact,"gender":gender,"age":age,"dob":dob,"email":email})
        a=open(filename,"w+")
        b=json.dumps(json_data,indent=2)
        a.write(b)
        print("congrats! your signup page succesfully")
    else:
        print("check the contact number")
# def login(filename):
#     user1=input("enter the user name:>")
#     password=input("enter the password")
#     json_data=read_data(filename)
#     for user in json_data:
#         if user ["name"]==user1:
#             break
#     else:
#         print("this user is not exist")
#         return " "
#     if user["password"]!=password:
#         print("please check your password")
#         return " "
#     print("login successfully")
def login(filename):
    user1=input("enter the user name")
    password=input("enter the password")
    with open("signup.json","r") as q:
        da=json.load(q)
        for i in range(len(da)):
            if da[i]["name"]==user1:
                if da[i]["password"]==password:
                    print("login successfully")
                    print("your name is",da[i]["name"],"\n")
                    # print("and your data is :-\n")
                    for x,y in da[i].items():
                        print(x,"=",y)
                else:
                    print("incorrect")
                    break
filename="signup.json"
file(filename)
print("WELCOME TO LOG IN SIGNUP")
choice=input("enter the choice:)signup[1],login[2]:>")
if choice=="1":
    signup(filename)
elif choice=="2":
    login(filename)
else:
    print("check your choice")