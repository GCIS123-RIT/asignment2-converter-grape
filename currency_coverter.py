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
                
    
def menu():
    print(aed_to_euro(5))

def main():
   menu()

main()