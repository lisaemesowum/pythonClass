
def check_password(check):
    password = "lisa1"
    
    
    if check != password:
        return "password invalid"
    else:
        return "password correct"
    

print(check_password("lisa1"))
    