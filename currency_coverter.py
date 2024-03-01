EURO_AED = 3.98
DOLLARS_AED = 3.67
POUNDS_AED = 4.65


def aed_to_euro(money):
    conv_currency = money * EURO_AED
    return conv_currency
    
    
def aed_to_british_pound(money):
    print('x')
    
    
    
def aed_to_dollar(money):
    print('x')
    
def dollar_to_aed(amount):
    print('x')
    
    
def british_pound_to_aed(amount):
    print('x')
    
    
def euro_to_aed(amount):
    print('x')


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