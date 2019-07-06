def turn_lamps(combination):
    lamps = [False] * 15
    combination = str(combination)
    for num in combination:
        if int(num) != 1:
            for i in range(1, 15 + 1):
                if i % int(num) == 0:
                    if lamps[i-1] == False:
                        lamps[i-1] = True
                    else:
                        lamps[i-1] = False
        else:
            if lamps[0] == False:
                lamps[0] = True
            else:
                lamps[0] = False
    return lamps


def main():
    print(turn_lamps(1321))


if __name__ == "__main__":
    main()
