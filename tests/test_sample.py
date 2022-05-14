from sample import main


def test_sample():
    ex = main()
    print("Running Test")
    assert ex == "Hello World"
