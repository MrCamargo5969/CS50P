from numb3rs import validate

def main():
    test_ip()
    test_variation()
    test_alpha()
    test_out_of_range()

def test_ip():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2.3.4.5') == False

def test_variation():
    assert validate('25.0.0.0') == True
    assert validate('0.0.0.25')
    assert validate('25.0.0.25') == True

def test_alpha():
    assert validate('cat') == False

def test_out_of_range():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('300.300.300.0') == False
    assert validate('0.0.0.300') == False

if __name__ == "__main__":
    main()
