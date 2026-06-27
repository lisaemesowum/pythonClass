
while True :
    print("--------------ATM SIMULATOR -------------------")
    print("1: Register")
    print("2: Login")
    print("3: Logout")
    choice = input("enter choice: ")
    if choice == "1":
        Personal_details = input("Personal Name: ")
        contact_info = input("Mobile Phone Number: ")
        # for the choose account type
        while True:
            print("-- Account Setup --")
            print("⭕ Choose Account Type -")
            print("1:Savings")
            print("2: Current")
        # while loop
            account = input("Choose Acount Type: ")
            if account == "1":
                account_setup = "Savings"
                break
            elif account == "2":
                account_setup = "Current"
                break
            else:
                 print("❌ Invalid choice. Please choose 1 or 2.\n")
         # This for the pin --------------------------   
        Pin = input("6-digit: ")
        # this for saving the details the user put in will be saved inthe log.txt
        with open("Aptech_FirstClass/File Handling/classwork/log.txt", "a") as file:
            file.write("-------------------------------------------------------------------------------\n")
            file.write("\n",f"Personal details - {Personal_details}\n\n")
            file.write("\n",f"Contact Info - {contact_info}\n\n")
            file.write("\n",f"Account Setup - {account_setup}\n\n")
            file.write("\n",f"Pin - {Pin}\n\n")
            # for the login
    elif choice == "2":
        username = input("Enter your name: ")
        pin = input("Enter Your 6 digit Pin: ")
        login_correct = False
        # read if the name and the pin is in the txt file ...............
        with open("Aptech_FirstClass/File Handling/classwork/log.txt", "r") as file:
          data = file.read()
        if f"Personal details - {username}"in data and f"Pin - {pin}"in data:
            login_correct = True
        
        if login_correct:
            print("Successful")
            with open("Aptech_FirstClass/File Handling/classwork/users.txt","w") as file:
                file.write("-------------------------------------------------------------------------------\n")
                file.writelines(f"username - {username}\n\n")
                file.writelines(f"Pin - {pin}\n\n")
                file.writelines(f"{username} login Successful. \n")
                # if loged in u do this..................
            while True:
                print("1: Deposited money")
                print("2: Checked balance")
                print("3: Withdrew money")
                print("4: Logged Out")
                decided = input("Options: ")
                if decided == "1":
                    balance = float(input("Deposit money:"))
                    
                    # check the exiting balace
                    with open("Aptech_FirstClass/File Handling/classwork/deposited.txt","r") as file:
                        lines = file.readlines()
                    for i in range(len(lines)):
                        if lines[i].strip() == f"username  - {username}":
                            balance_line = i + 2
                            old_balance = float(lines[balance_line].split("-")[1].strip())
                            new_balance = old_balance + balance
                            lines[balance_line] = f"balance - {new_balance}\n"
                            break
                    with open("Aptech_FirstClass/File Handling/classwork/deposited.txt","w") as file:
                        file.writelines(lines)
                    with open("Aptech_FirstClass/File Handling/classwork/deposited.txt","a") as file:
                        file.write("-------------------------------------------------------------------------------\n")
                        file.writelines(f"{username} deposited {balance}\n")
                        print("deposited")
                       
                if decided == "2":
                    with open("Aptech_FirstClass/File Handling/classwork/deposited.txt","r") as file:
                        lines = file.readlines()
                        
                    for i in range(len(lines)):
                        if lines[i].strip() == f"username - {username}":
                            balance = lines[i + 2].split("-")[1].strip()
                            print(f"your balance is ₦{balance}")
                        with open("Aptech_FirstClass/File Handling/classwork/Checked_balance.txt","w") as file:
                            file.write("-------------------------------------------------------------------------------\n")
                            file.write(f"{username} is  your account balance is - {balance}.\n")
                        break
                    
                elif decided == "3":
                    amount = float(input("How much to withdraw?: "))
                    with open("Aptech_FirstClass/File Handling/classwork/users.txt","r") as file:
                        lines = file.readlines()
                    for i in range(len(lines)):
                        if lines[i].strip() == f"username - {username}":
                            balance_line = i + 2
                            old_balance = float(lines[balance_line].split("-")[1].strip())
                            if amount > old_balance:
                                print("No Money")
                            else:
                                new_balance = old_balance - amount
                                lines [balance_line] =  f"balance - {new_balance}\n"
                                with open("Aptech_FirstClass/File Handling/classwork/deposited.txt","w") as file:
                                    file.writelines(lines)
                                    
                                
                                with open("Aptech_FirstClass/File Handling/classwork/withdrawal.txt","a") as file:
                                    file.writelines(f"{username} withdraw {amount}\n")
                        break
                elif decided == "4" :
                    print("logout successful")
                    with open("Aptech_FirstClass/File Handling/classwork/logout.txt","a") as file:
                     file.write("-------------------------------------------------------------------------------\n")
                     file.write(f"{username} logged out.\n")
                    break
                        
                    
                                      
                          

                    
                        
                        
                        
                    
                    
                   
            
        else:
           print("failed")
            
           with open("Aptech_FirstClass/File Handling/classwork/users.txt","w") as file:
               file.writelines(f"login failed, try again {username} \n\n") 
               
        break
        
        
    
            
            
    
        