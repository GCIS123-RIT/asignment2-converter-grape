import currency_coverter

def test_error_handeling_True():
    EXPECTED = True
    actual = currency_coverter.error_handler(6)
    
    assert EXPECTED == actual
    
def test_error_handeling_False():
    EXPECTED = False
    actual = currency_coverter.error_handler("Hello")
    
    assert EXPECTED == actual

