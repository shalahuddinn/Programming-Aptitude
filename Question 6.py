# Source: stackoverflow.com/questions/27074649/generating-permutations-using-bitmasking


def permutations():
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        print(''.join(running))
    else:
        for i in range(len(characters)):
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations()
                bitmask ^= 1 << i # answer
                running.pop()

f = open("input6.in", "r")
raw = f.readline()[:-1]
characters = list(raw)
running = []
bitmask = 0
permutations()
