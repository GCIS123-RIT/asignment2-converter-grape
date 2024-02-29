import currency_coverter
EURO_AED = 3.98
DOLLARS_AED = 3.67
POUNDS_AED = 4.65

def test_error_handeling_True():
    EXPECTED = True
    actual = currency_coverter.error_handler(6)
    
    assert EXPECTED == actual
    
def test_error_handeling_False():
    EXPECTED = False
    actual = currency_coverter.error_handler("Hello")
    
    assert EXPECTED == actual

def test_negative_False():
    EXPECTED = False
    actual = currency_coverter.check_negative(-1)
    
    assert EXPECTED == actual
def test_positive_True():
    EXPECTED = True
    actual = currency_coverter.check_negative(2)
    
    assert EXPECTED == actual

def test_string_False():
    EXPECTED = False
    actual = currency_coverter.check_negative("Hello")
    
    assert EXPECTED == actual

def test_aed_to_euro():
    EXPECTED = 5 * EURO_AED
    actual = currency_coverter.aed_to_euro(5)
    
    assert EXPECTED == actual