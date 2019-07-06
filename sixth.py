def turn_lamps(combination):
    lamps = [False] * 15
    combination = str(combination)
    for num in combination:
        number_in_combination = int(num)
        assert 1 <= number_in_combination <= 3
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

    on = 0
    off = 0

    for i in lamps:
        if i == True:
            on += 1
        else:
            off += 1

    print(lamps)
    print('Jumlah lampu menyala: {}'.format(on))
    print('Jumlah lampu mati: {}'.format(off))


def main():
    turn_lamps(1321)


if __name__ == "__main__":
    main()
