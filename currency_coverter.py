#Ameen Ahmed
#Pranav Anil
#Ali Alblooshi
#Mohammed Daaboul

import sys

"""Conversion rates of different currencies to AED"""
EURO_AED = 3.98     # conversion rate - euro to aed
DOLLARS_AED = 3.67  # conversion rate - pound to aed
POUNDS_AED = 4.65   # conversion rate - dollar to aed

"""AED to Euro by dividing amount of money entered by the user with Euro Rate"""
def aed_to_euro(money):
    conv_currency = money / EURO_AED

    return conv_currency
    
"""AED to Pound by dividing amount of money entered by the user with Pound Rate"""
def aed_to_british_pound(money):
    conv_currency  = money / POUNDS_AED

    return conv_currency
    
"""AED to Dollar by dividing amount of money entered by the user with Dollar Rate"""
def aed_to_dollar(money):
    conv_currency = money / DOLLARS_AED 

    return conv_currency

"""Dollar to AED by multiplying amount of money entered by the user with Dollar Rate"""
def dollar_to_aed(amount):  
    conv_currency = amount * DOLLARS_AED

    return conv_currency    
    
"""Pound to AED by multiplying amount of money entered by the user with Pound Rate"""
def british_pound_to_aed(amount):
    conv_currency = amount * POUNDS_AED

    return conv_currency

"""Euro to AED by multiplying amount of money entered by the user with Euro Rate"""    
def euro_to_aed(amount):
    conv_currency =  amount * EURO_AED

    return conv_currency

def error_handler(money):

    try:
        a = int(money)
        return True
    
    except:
        return False
       
def check_negative(money):
    
    if error_handler(money) is True:
        if money <1:
            return False
        else:
            return True
    
    return False 
                
"""AED to other currencies conversions"""
def aed_to_other_menu(money): #If user wishes to convert from AED to other currencies
    print("1. AED to Euro (EUR)")
    print("2. AED to British Pound (GBP)")
    print("3. AED to US Dollar")

    target_currency = input("Enter the target currency from the above menu - choice (1/2/3): ") # Asking the user for their choice
    print("---------------------------------")
    print("")

    if target_currency == "1":  
        converted_amount = aed_to_euro(money) #converting AED to Euro
        print(str(money) + " AED is equal to " + str(converted_amount) + " EUR")
    elif target_currency == "2":
        converted_amount = aed_to_british_pound(money) #converting AED to Pound
        print(str(money) + " AED is equal to " + str(converted_amount) + " GBP")
    elif target_currency == "3":
        converted_amount = aed_to_dollar(money) #converting AED to Dollar
        print(str(money) + " AED is equal to " + str(converted_amount) + " USD")
    else:
        print("Invalid Choice") #If user enters any number other than 1,2,3
    
    print("---------------------------------")


"""Other currencies to AED conversions"""
def other_to_aed_menu(money): #If user wishes to convert from other currencies to AED
    print("1. Euro to AED ")
    print("2. British Pound to AED ")
    print("3. US Dollar to AED ")

    target_currency = input("Enter the target currency from the above menu - choice (1/2/3): ") # Asking the user for their choice
    print("---------------------------------")
    print(" ")

    if target_currency == "1":
        convert_amount = euro_to_aed(money) #converting Euro to AED
        print(str(money) + " Euro is equal to " + str(convert_amount) + " AED")
    elif target_currency == "2":
        convert_amount = british_pound_to_aed(money) #converting Pound to AED
        print(str(money) + " GBP is equal to " + str(convert_amount) + " AED")
    elif target_currency == "3":
        convert_amount = dollar_to_aed(money) #converting Dollar to AED
        print(str(money) + " USD is equal to " + str(convert_amount) + " AED")
    else:
        print("Invalid choice") #If user enters any number other than 1,2,3
    print("---------------------------------")

def main_menu():
    print("---------------------------------")
    print("           Main Menu             ")
    print("  Welcome to Currency Converter  ")
    print("---------------------------------")
    print("  ")
    print("  ")

    print("1. AED to other currencies")   #If user wishes to convert from AED to other currencies
    print("2. Other currencies to AED")   #If user wishes to convert from other currencies to AED
    print("3. Exit")                      #If user wishes to exit from the converter

    while True:
        money_amount = input("Enter the amount you want to convert: ")   # Asking the user for the amount which they wish to convert.
        if error_handler(money_amount) == True and check_negative(money_amount) == True:
            money = int(money_amount)
            break
        elif money_amount == "e":
            sys.exit()

        else:
            print(" ")
            print("please enter a valid amount or type 'e' to EXIT")
            print(" ")

    convert_choice = int(input("Enter the conversion direction - choice (1/2/3): ")) # Asking the user for their choice
    print("---------------------------------")
    print("")

    if convert_choice == 1: #If user wants to convert AED to other currencies
        aed_to_other_menu(money) 
    elif convert_choice == 2: #If user wants to convert amount to AED
        other_to_aed_menu(money)
    elif convert_choice == 3: #If the user wants to exit the converter
        print("Byee!!!! Thankyou for using this service ")
        sys.exit()
    else:
        print("invalid choice") #If user enters anything other than 1,2,3

def main():
    while True:
       main_menu()
