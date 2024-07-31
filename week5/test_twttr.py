from twttr import shorten

def main():
    test_upper_lower_cases()
    test_numbers()
    test_punc()

def test_upper_lower_cases():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("tIwTtEr") == "twTtr"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punc():
    assert shorten("!?.,") == "!?.,"

if __name__ == "__main__":
    main()
