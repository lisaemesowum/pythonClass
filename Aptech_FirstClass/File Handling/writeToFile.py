with open("Aptech_FirstClass/File Handling/report.txt","w") as file:
    file.write("This is weekly reports")
    

states = [
    "Abia State\n",
    "Adamawa State\n",
    "Akwa Ibom State\n",
    "Anambra State\n",
    "Bauchi State\n",
    "Bayelsa State\n",
    "Benue State\n",
    "Borno State\n",
    "Cross River State\n",
    "Delta State\n",
    "Ebonyi State\n",
    "Edo State\n",
    "Ekiti State\n",
    "Enugu State\n",
    "Gombe State\n",
    "Imo State\n",
    "Jigawa State\n",
    "Kaduna State\n",
    "Kano State\n",
    "Katsina State\n",
    "Kebbi State\n",
    "Kogi State\n",
    "Kwara State\n",
    "Lagos State\n",
    "Nasarawa State\n",
    "Niger State\n",
    "Ogun State\n",
    "Ondo State\n",
    "Osun State\n",
    "Oyo State\n",
    "Plateau State\n",
    "Rivers State\n",
    "Sokoto State\n",
    "Taraba State\n",
    "Yobe State\n",
    "Zamfara State\n",
    "Federal Capital Territory (FCT)\n"
]
with open("Aptech_FirstClass/File Handling/report.txt","w") as file:
    file.writelines(states)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # # check the user amount
    #                 start = data(f"Personal Details - {username}")
    #                 if start != -1:
    #                     balance_start = data.find("Balance - ", start)
    #                     balance_end = data.find("\n", balance_start)
    #                     old_balance = float(data[balance_start + 10:balance_end])
    #                     new_balance = old_balance + money
    #                     # replacing the existing amount with the new
    #                     data = data.replace(
    #                         f"Balance - {old_balance}",
    #                         f"Balance - {new_balance}",
    #                         1
    #                     )
    #                     with open("Aptech_FirstClass/File Handling/classwork/log.txt", "w") as file:
    #                      file.write(data)
    #                      # Log the transaction
    #                     with open("Aptech_FirstClass/File Handling/classwork/log.txt", "a") as file:
    #                         file.write(f"{username} deposited {money}\n")

    #                 print(f"Deposit successful.")
    #                 print(f"New Balance: {new_balance}")

