def login_cr(username: str, password: str) ->bool: #define a fucntion for login credtentials
    is_authenticated= False# initialixze it to false

    if username== "admin" and password== "1234":
       is_authenticated= True# if this is the respective username and password

    return is_authenticated    

user=input("enter the username")
passw=input("enter the password")
attempts=1
max_attempts=5
is_authenticated=False
while login_cr(user,passw)==False :
    attempts+=1
    if attempts> max_attempts: break

    print("login failed, please check your username or password:")
    user=input("enter the username")
    passw=input("enter the password")
else:
        is_authenticated= True
        print("login succesfull")

        if not is_authenticated:
            print("account temporarily locked")
