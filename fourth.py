def buyNoodle(date, money):
    price = 1650
    amount = money // price
    if date % 5 == 0:
        if date % 2:
            bonus = amount // 3
            amount = amount + (bonus*5)
        else:
            bonus = amount // 4
            amount = amount + (bonus*10)
    else:
        if date % 2:
            bonus = amount // 3
            amount = amount + bonus
        else:
            bonus = amount // 4
            amount = amount + bonus
    return amount


def main():
    print(buyNoodle(25, 50000))


if __name__ == "__main__":
    main()
