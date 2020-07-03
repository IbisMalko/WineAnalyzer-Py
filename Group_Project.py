# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:37:09 2017

@author: Ibis.Malko
"""

import sqlite3
import sys 


"""
Test Login Credentials:
Email = "belle.bristow@gmail.com"
testpassword = "belle"
"""

    
#Collect password and email from user
def get_login():
    userEmail = input("-------------------------\n" +
                      "|     PLEASE LOGIN      |\n" +
                      "-------------------------\n" +
                      "\nEnter 'q' or 'quit' to exit.\n\n"+
                      "Please enter your email: ")
    if userEmail.lower() == 'q' or userEmail.lower() == 'quit':
        sys.exit()
    userPassword = input("Please enter your password: ")
    if userPassword.lower() == 'q' or userPassword.lower() == 'quit':
        sys.exit()
    #if userPassword.lower() == 'q' or userPassword.lower() == 'quit' or userEmail.lower() == 'q' or userEmail.lower() == 'quit':
    
    conn= sqlite3.connect('LeVinEmployee.db')

    with conn:  
        cur = conn.cursor()
        try:
            #select password and email from employee database
            cur.execute("Select Count('EmployeeID') FROM Employee WHERE (Email = '" + userEmail.lower() + "') AND (Password = '" + userPassword.lower() + "')")
            #Gather all results from employee database
            results = cur.fetchall()
            #print (results[0][7])
            #password = results[0][8]
            cur.execute("Select * FROM Employee WHERE (Email = '" + userEmail.lower() + "') AND (Password = '" + userPassword.lower() + "')")
            UserInformation = cur.fetchall()
            global userFirstName 
            userFirstName = UserInformation[0][1]
            global userLastName 
            userLastName = UserInformation[0][2]
            if results == [(1,)]:
                login = True
            else:
                login = False
                print ("\n--Incorrect Email or Password.\nPlease Try again!\n")
            return login
        
        except Exception as e:
            login = False
            print ("\nPlease enter the correct login credentials")
            return login
    
        
def register():
    print ( "\n\n------------------------------\n" +
            "|    REGISTER A NEW USER     | \n" + 
            "------------------------------" )
    
    conn= sqlite3.connect('LeVinEmployee.db') 
        
    regEmployeeID = input("Please enter the empolyee's ID: ")
    regFirstName = input("Please enter the first name of the user that you will like to register: ")
    regLastName = input("Please enter the last name of the user that you will like to register: ")
    regStreetAddress = input("Please enter their street address: ")
    regCity = input ("Please enter the city of their address: ")
    regState = input("Please enter the abbreviated state of their address: ")
    regZipCode = input("Please enter their zip code: ")
    regEmail = input("Please enter their email address: ")
    regPassword = input("Please enter their password: ")
    
    
    with conn: 
        
        cur = conn.cursor()
        cur.execute("Insert Into Employee Values ('" + regEmployeeID + "', '" +
                                           regFirstName.title() + "', '" + 
                                           regLastName.title() + "', '" + 
                                           regStreetAddress + "', '" +
                                           regCity.title() + "', '" +
                                           regState.upper() + "', '" +
                                           regZipCode + "', '" +
                                           regEmail.lower() + "', '" +
                                           regPassword + "')") 
    conn.commit()
    
    print ( "\n\n--" + regFirstName.title() + " " + regLastName.title() + " was successfully registered!\n")
    
    menu ()
        
def Main():
    while get_login() == False :
        get_login()
    print ( "\n\n-------------------------------\n" +
           "|     LOGIN WAS SUCCESSFUL    | \n" + 
           "-------------------------------\n\n" )
    print ("--Welcome " + userFirstName.title() + " " + userLastName.title() + "!\n")
    
    menu()


def menu():

    print ( "\n\n------------------------------\n" +
            "|          DIRECTORY         | \n" + 
            "------------------------------\n" )
    print ("1 = Register User")
    print ("2 = Logon as a Different User")
    print ("3 = Get Wine Data Correlations")
    print ("4 = Choose Wine Characteristics")
    print ("5 = Anaylze Frequency of Wine Characteristics")
    print ("6 = Exit")
    
    option = input("Please enter one of the above numbers: ")
    
    if option == "1":
        register()
    elif option == "2":
        Main()
    elif option == "3":
        wineTypePref = input("What type of wine are you correlating?\n" +
                             "Please enter 'Red' or 'White': ")
        if wineTypePref.lower() == "red" or wineTypePref.lower() == "r":
            get_WineCSV("red")
        elif wineTypePref.lower() == 'white' or wineTypePref.lower() == 'w':
            get_WineCSV("white")
        else:
            print ("Wine Type was invalid.")
            menu()
    elif option == "4":
        get_WineChar()
    elif option == "5":
        wineTypePref = input("What type of wine are you correlating?\n" +
                             "Please enter 'Red' or 'White': ")
        if wineTypePref.lower() == "red" or wineTypePref.lower() == "r":
            get_WineFreq("red")
        elif wineTypePref.lower() == 'white' or wineTypePref.lower() == 'w':
            get_WineFreq("white")
        else:
            print ("Wine Type was invalid.")
            menu()
    elif option == "6":
        sys.exit()
    else:
        menu()
        
        
def get_WineChar():
    
    global firstChar
    global secondChar
    global WineCharX
    global WineCharY
    
   
    while True:
        try:
            wine_Chars = {
           '1': 'fixed acidity',
           '2': 'volatile acidity',
           '3': 'citric acid',
           '4': 'residual sugar',
           '5': 'chlorides',
           '6': 'free sulfur dioxide',
           '7': 'total sulfur dioxide',
           '8': 'density',
           '9': 'pH',
           '10': 'sulphates',
           '11': 'alcohol',
           '12': 'quality',
           }
   
            print ( "\n\n----------------------------------------------------\n" +
                   "|          Select First Wine Characteristic        | \n" + 
                   "----------------------------------------------------\n" )

            for key, char in wine_Chars.items():
                if key != "9":
                    print (key +" = " + char.title())
                else:
                    print (key +" = " + char)
            
            firstChar = int(input('Out of these options (1-12), please select one wine characteristic: '))
            break
        except:
            print("That's not a valid option!")

    if int(firstChar) >= 1 and int(firstChar) < 13:
        WineCharX = wine_Chars.get(str(firstChar))
        wine_Chars.pop(str(firstChar))
        while True:
            try:
                print ( "\n\n-----------------------------------------------------\n" +
                       "|          Select Second Wine Characteristic        | \n" + 
                       "-----------------------------------------------------\n" )
    
                for key, char in wine_Chars.items():
                    if key != "9":
                        print (key +" = " + char.title())
                    else:
                        print (key +" = " + char)
                
                secondChar = int(input('Out of the remaining options (1-12), please select one wine characteristic: '))
                break
            except:
                print("That's not a valid option!")

        if secondChar >= 1 and secondChar < 13 and secondChar != firstChar:
            WineCharY = wine_Chars.get(str(secondChar))
            print("\nYour Wine Characteristics are "+ WineCharX +" and " + WineCharY +"!\n")
            menu()
        else:
            print("That's is not a valid option, please try again.")
            get_WineChar()        
        
    else:
        print("That's is not a valid option, please try again.")
        get_WineChar()
        
    
       
        
def get_WineCSV(typePref):
    import pandas as WineData
    import scipy.stats
    import seaborn
    import matplotlib.pyplot as plot
    #from pylab import savefig
    #from PIL import Image
    global allWines
    global red
    global white
    global getCorrelation
    global pValue
    global correlation
    global dataType
    
    
    
    #WineCharX = "quality"
    #WineCharY = "volatile acidity"
    #input Wine CSV
    allWines = WineData.read_csv('winequality-both.csv')
    #Split Wine type Data into one dataset, red or white based on augrument
    dataType = allWines.loc[allWines['type']==typePref,:]
    
    getCorrelation = scipy.stats.spearmanr(dataType [ WineCharX ], dataType [ WineCharY ])
    correlation = str(getCorrelation[0])
    pValue = str(getCorrelation[1])
    print ("\n\nFor " + typePref.title() + " wine:\n\nThe Correlation between " + WineCharX.title() + 
           " and " + WineCharY.title() +" is " + correlation + ".")
    print ("With a Probability Value of " + pValue + ".")
    
    seaborn.lmplot(x=WineCharX, y=WineCharY, data=dataType)
    plot.xlabel(WineCharX.title())
    plot.ylabel(WineCharY.title())
    plot.title(typePref.title() + " Wine: " + WineCharX.title() + " X " + WineCharY.title())
    #savefig("scatterplot1.png")
    plot.show()
    menu()        
    
def  get_WineFreq(typePref):
    import pandas
    import matplotlib.pyplot as plot
    import seaborn
    
    global firstChar
    global secondChar
    global WineCharX
    global WineCharY
    
    
    
    wineCharsMin = {
        '1': 3.8,
        '2': 0.08,
        '3': 0,
        '4': 0.6,
        '5': 0.009,
        '6': 1,
        '7': 6,
        '8': 0.98711,
        '9': 2.72,
        '10': 0.22,
        '11': 8,
        }
    wineCharsMax = {
        '1': 15.9,
        '2': 1.58,
        '3': 1.66,
        '4': 65.8,
        '5': .611,
        '6': 289,
        '7': 440,
        '8': 1.03898,
        '9': 4.01,
        '10': 2,
        '11': 14.9,
        }
    
    while True:
        try:
            wine_Chars = {
                    '1': 'fixed acidity',
                    '2': 'volatile acidity',
                    '3': 'citric acid',
                    '4': 'residual sugar',
                    '5': 'chlorides',
                    '6': 'free sulfur dioxide',
                    '7': 'total sulfur dioxide',
                    '8': 'density',
                    '9': 'pH',
                    '10': 'sulphates',
                    '11': 'alcohol',
           }
   
            print ( "\n\n----------------------------------------------------\n" +
                   "|            Select a Wine Characteristic          | \n" + 
                   "----------------------------------------------------\n" )

            for key, char in wine_Chars.items():
                if key != "9":
                    print (key +" = " + char.title())
                else:
                    print (key +" = " + char)
            
            firstChar = int(input('Out of these options (1-11), please select one wine characteristic: '))
            break
        except:
            print("That's not a valid option!")
    
    if int(firstChar) >= 1 and int(firstChar) < 12:
        WineCharX = wine_Chars.get(str(firstChar))
        WineCharY = "quality"
        print("\nYour Wine Characteristics are "+ WineCharX +" and " + WineCharY +"!\n")
    else:
        print("That's is not a valid option, please try again.")
        get_WineFreq()
    
    while True:
        try:
            print ("Your input range for " + WineCharX + " is: " + str(wineCharsMin.get(str(firstChar))) + " to " + str(wineCharsMax.get(str(firstChar))) + " !"  )
            wineCharValue = input("\nPlease enter the value you want to quantify for " + WineCharX + ": ")
            if float(wineCharValue) >= wineCharsMin.get(str(firstChar)) and float(wineCharValue) <= wineCharsMax.get(str(firstChar)) : 
                break
        except:
            print("That's not a valid option!")
    
    allWines = pandas.read_csv('winequality-both.csv')
    #Split Wine type Data into one dataset, red or white based on augrument
    dataType = allWines.loc[allWines['type']==typePref,:]
    dataChar = dataType.loc[dataType[WineCharX]==float(wineCharValue),WineCharY]
    seaborn.distplot(dataChar, bins=10,kde=False)
    plot.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    plot.ylabel('Number of Wines')
    plot.title(typePref.title() + " Wine: " + WineCharX.title() + " value  "+ str(wineCharValue) +" frequenies by " + WineCharY.title())
    plot.show()
    menu()
    
    
    
#default Wine Characteristics
WineCharX = "fixed acidity"
WineCharY = "volatile acidity"

Main()
#WineCharX = "quality"
#WineCharY = "volatile acidity"


