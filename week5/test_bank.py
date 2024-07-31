from bank import value
def main():
    test_valuer_0()
    test_valuer_20()
    test_valuer_100()

def test_valuer_0():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_valuer_20():
    assert value("hi") == 20
    assert value("Hi") == 20

def test_valuer_100():
    assert value("whats up") == 100
    assert value("Whats up") == 100

if __name__ == "__main__":
    main()
