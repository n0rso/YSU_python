from productcheck import check


def buy(product, num, price):
    if check(product, num) == True:
        spent = num * price
        print("You bought product and spent ", spent)
    else:
        print("Sorry!We are out of this product")


def main():
    buy("pen", 5, 5)


if __name__ == '__main__':
    main()