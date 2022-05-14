"""
Sample Project using Python
"""


class Sample:
    """
    Sample Class
    """

    def __init__(self):
        """
        Constructor
        """
        print("Sample Class")

    def welcome(self):
        """
        Welcome Message
        """
        return "welcome"


class Sample2(Sample):
    """
    Sample Class
    """

    def __init__(self):
        """
        Constructor
        """
        print("Sample Class")

    def hello(self):
        """
        Hello Message
        """
        return "Hello"


def main():
    """
    Main function
    """
    sample = Sample()
    sample2 = Sample2()
    print(sample.welcome())
    print(sample2.welcome())
    print(sample2.hello())
    return "Hello World"


if __name__ == "__main__":
    main()
