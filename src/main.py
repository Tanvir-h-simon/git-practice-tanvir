from datetime import date

from utils import add, subtract


def main():
    print("Name: Tanvir Hossain")
    print("Today's date:", date.today())

    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))


if __name__ == "__main__":
    main()
