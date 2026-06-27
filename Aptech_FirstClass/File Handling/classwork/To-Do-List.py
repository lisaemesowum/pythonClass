

while True:
    print("\n============== Football Survey==================")
    print("1:Add your answers")
    print("2: exit")
    choice = input("Please your choice: ")
    
    if choice == "1":
        best_football = input("Add your best footballer: ")
        best_club = input("Best Club: ")
        world_club = input("Who will win the Fifa Would Cup 2026?: ")
        with open("Aptech_FirstClass/File Handling/classwork/audittrail.txt","a") as file:
          file.write(f"Best Football Player - {best_football}\n")
          file.write(f"Best Football Club - {best_club}\n")
          file.write(f"World Cup Winner - {world_club}\n")
    elif choice == "2":
        print("Have a nice day")
        break
    else:
     print("invalid choice")
     
        
        
        
