def nameScore(name):
    splited = name.split(" ")
    multiplier = 1
    score = []
    for i in splited:
        total = 0
        for j in i:
            total += (ord(j.lower()) - 97 + 1)
        score.append(total * multiplier)
        multiplier += 1
    return score


def main():
    name = input('Name: ')
    print(nameScore(name))


if __name__ == "__main__":
    main()
