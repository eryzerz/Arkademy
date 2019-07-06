def steps(num, count=0):
    if num == 1:
        return count
    else:
        if num % 2 == 0:
            return steps(num // 2, count + 1)
        if num % 2 == 1:
            return steps(3 * num + 1, count + 1)


def operation(limit):
    biggest = steps(1)
    num = 0
    for i in range(1, limit + 1):
        if steps(i) > biggest:
            biggest = steps(i)
            num = i
    return num


def main():
    print(operation(100))


if __name__ == "__main__":
    main()
