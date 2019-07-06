def buyNoodle(date, money):
    assert 1 <= date <= 30
    price = 1650
    amount = money // price
    if date % 5:
        if date % 2:
            bonus = amount // 3
            amount = amount + bonus
        else:
            bonus = amount // 4
            amount = amount + bonus
    else:
        if date % 2:
            bonus = amount // 3
            amount = amount + (bonus*5)
        else:
            bonus = amount // 4
            amount = amount + (bonus*10)
    return amount


def main():
    print(buyNoodle(30, 50000))


if __name__ == "__main__":
    main()
