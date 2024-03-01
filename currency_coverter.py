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

