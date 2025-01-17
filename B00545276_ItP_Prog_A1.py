# Intro to Programming Assessment 1 B00545276

import pickle


#Pickle Load and Display User Data
def admin_printUsers():
    with open('B00545276_ItP_Prog_A1.pkl', 'rb') as file:
        admin_printUsersData = pickle.load(file)
    print ("Registered Users: ", admin_printUsersData) 

#Pickle Dump


#Initial start menu
def start_menu():
    print ("--Title--")

    print ("(1) - Login")
    print ("(2) - Register")
    print ("(3) - Admin")
    print ("(x) - Exit")

    start_menuInput = input ("Enter corrisponding option number of desired choice >>>")

    if start_menuInput == ("1"):
        login_menu()
    elif start_menuInput == ("2"):
        register_menu()
    elif start_menuInput == ("3"):
        admin_login()
    elif start_menuInput == ("x") or start_menuInput == ("X"):
        close()
    else:
        print ("Enter one of the avaliable options")
        start_menu() 

#Login Menu
def login_menu():
    print ("Login: ")
    

#Register Menu
def register_menu():
    print ("Register:")
    print ("Enter 'x' to return to main menu")
    
    foreName = str (input ("Enter your forename: "))
    if foreName == ("x") or foreName == ("X"):
        start_menu()
        
    surName = str (input ("Enter your surname: "))
    if surName == ("x") or surName == ("X"):
        start_menu()

    dayOfBirth = str (input ("Enter your Day of Birth (DD): "))
    if dayOfBirth == ("x") or dayOfBirth == ("X"):
        start_menu()

    monthOfBirth = str (input ("Enter your Month of Birth (MM): "))
    if monthOfBirth == ("x") or monthOfBirth == ("X"):
        start_menu()

    yearOfBirth = str (input ("Enter your Year of Birth (YYYY): "))
    if yearOfBirth == ("x") or yearOfBirth == ("X"):
        start_menu()


    fullDOB = (dayOfBirth[0:3] + "/" + monthOfBirth[0:3] + "/" yearOfBirth[0:5])
    userName = (foreName[0:3] + surName[0:3] + dayOfBirth[0:2] + monthOfBirth[0:2])
    
    print ("Your username is - ", userName)
    print ("Enter your desired username. It must be 6-12 characters and have at least 1 uppercase letter, 1 lowercase letter and 1 number.")
    user_password = str (input("Password >>>"))

    userInfo = [foreName, surName, fullDOB, userName]
    
    return userInfo


#Admin Login
def admin_login():
    print ("Admin Login:")
    admin_user = str (input ("Admin username: "))
    admin_pass = str (input ("Admin password: "))

    if admin_user == ("monty") and admin_pass == ("python"):
        admin_menu()
    else:
        print ("Login details incorrect. Please try again")
        admin_login()

#Admin Menu
def admin_menu():
    print ("Admin Menu: ")
    print ("(1) - Display Registered Users")
    print ("(x) - Return")

    admin_menuInput = input ("Enter option from menu >>>")

    if admin_menuInput == ("1"):
        admin_printUsers()
    elif admin_menuInput == ("x") or admin_menuInput == ("X"):
        start_menu()
    else:
        print ("Enter an avaliable menu option")
        admin_menu()

#Close Function