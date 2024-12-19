username1 = []
password1 = []
Grades = []

view_choice = (input("Do you want to view your login system options?(Yes/No) "))
if view_choice == "Yes".lower():
     while True:
          print("1.) Register \n2.) Login \n3.) Reset \n4.) Exit")
          choice = (input("Enter a number of your choice: "))

          if choice == "1":
            print("You have chosen to register.")
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            
            if username in username1:
                print("Username already exist. Please try a different one.")
            if password in password1:
                print("Password already exist. Please try a different one.")
            else:
                print("You have successfully registered!")
                username1.append(username)
                password1.append(password)

          elif choice == "2":
            print("You have chosen to login.")
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username in username1:
                print("Correct username entered!.")
            if password in password1:
                print("Correct password entered!.")
                print("Login successfully!")

                while True:
                  Input = input("Welcome to the Grade Tracker.   \nChoose an Option:  \n1. Add Grades\n2. Remove a grade\n3. Calculate average grade\n4. Display highest and lowest grade\n5. Display all grades\n6. Logout\nYour Choice: ")
                    
                  if Input == "1":
                    Add = int(input("Input a grade to add to the system: "))
                    if 40 <= Add <= 100:
                      Grades.append(Add)
                      print(f"Current Grades: {Grades}")
                    else:
                      print("Invalid Grade Input. Please enter a grade between 40 and 100.")

                  elif Input == "2":
                    if Grades:
                      print(f"Current Grades: \n{Grades}")
                      remove = int(input("Choose a Grade to remove: "))
                      if remove in Grades:
                        Grades.remove(remove)
                        print(f"{remove} has been removed from the grade list.\nCurrent Grade List: {Grades}")
                      else:
                        print(f"{remove} is not in the grade list.")
                    else:
                      print("No grades are available to remove.")

                  elif Input == "3":
                    if Grades:
                      total_sum = sum(Grades)
                      average = total_sum / len(Grades)
                      print(f"Computed Grade Average is {average:.2f}")
                    else:
                      print("No grades in the system to compute the average of.")

                  elif Input == "4":
                    if Grades:
                      minimum = min(Grades)
                      maximum = max(Grades)
                      print(f"Grade Analysis: \nHighest: {maximum} \nLowest: {minimum}")
                    else:
                     print("No grades to analyze.")
    
                  elif Input == "5":
                    if Grades:
                      print(f"All Grades: {Grades}")
                    else:
                      print("No grades are in the list.")
    
                  elif Input == "6":
                    print("Thank you for using Grade Tracker. Logging off...")
                    break
    
                  else:
                    print("Invalid input, please try again.")
            else:
                print("Incorrect username/password. Please try again.")
          elif choice == "3":
            remove_user = 1
            for task in username1 and password1:
                print(f"{remove_user}. {task}")
                remove_user += 1

            remove_prompt = int(input("Enter a username number to remove:"))
            if remove_prompt <= len(username1) and len(password1):
                del username1[remove_prompt - 1]
                del password1[remove_prompt - 1]
                print("User removed successfully")

            else:
                print("Invalid input, Please try again.")

          elif choice == "4":
            print("Thank you!")
            break

          else:
              print("Invalid input, Please try again.")

else:
    print()