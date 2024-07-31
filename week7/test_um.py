from um import count

def main():
    test_match()
    test_regex()
    test_case_insensitive()

def test_match():
    assert count('um, Um, uM, UM,') == 4

def test_regex():
    assert count(' um , um? um...') == 3

def test_case_insensitive():
    assert count('yum, mum') == 0

if __name__ == "__main__":
    main()
