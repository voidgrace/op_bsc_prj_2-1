pos = [0]*8


def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            set(i+1)


set(0)