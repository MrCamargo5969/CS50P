from plates import is_valid
def main():
    test_max_min()
    test_starts_plate()
    test_numbers_end()
    test_first_number()
    test_punc()

def test_max_min():
    assert is_valid("AA") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AABBCCD") == False
    assert is_valid("A") == False

def test_starts_plate():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_numbers_end():
    assert is_valid("AA2020") == True
    assert is_valid("AAA202") == True
    assert is_valid("AAAA20") == True
    assert is_valid("AAAAA2") == True

    assert is_valid("AA202A") == False
    assert is_valid("AA20AA") == False
    assert is_valid("AA2AAA") == False

def test_first_number():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punc():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI3,14") == False
    assert is_valid("PI3 14") == False
    assert is_valid("PI3 14") == False

if __name__ == "__main__":
    main()
