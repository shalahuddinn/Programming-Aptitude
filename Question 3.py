# Modification From https://github.com/jojoarianto/online-test-1/blob/master/q5.go

import sys
sys.setrecursionlimit(10000) #Sometimes we need more limit on recursion


def isConflicted(army, x_location, y_location, grid, flag):
    direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    R = len(grid)
    C = len(grid[0])
    current = grid[y_location][x_location]
    if current != "." and current != army:
        flag = True
    grid[y_location][x_location] = "!"
    # for y in range(len(grid)):
    #     for z in grid[y]:
    #         print(z, end='')
    #     print()
    for x, y in direction:
        x_editted, y_editted = x_location + x, y_location + y
        if 0 <= x_editted < C and 0 <= y_editted < R:
            next = grid[y_editted][x_editted]
            if next != "#" and next !="!":
                result = isConflicted(army, x_editted, y_editted, grid, flag)
                flag = result
    return flag




if __name__ == '__main__':
    f=open("input3.in", "r")
    final_result = 0
    grid_list = []
    letters_list = []
    word_list = []
    # T = int(input())
    T = int(f.readline())

    for i in range(T):
        # N = int(input())
        # M = int(input())
        N = int(f.readline())        # row
        M = int(f.readline())        # column
        for y in range(N):
            # letters = list(input())
            letters = list((f.readline())[:-1])
            # print(letters)
            letters_list.append(letters)
            # print(letters_list)

        grid_list.append(letters_list)
        letters_list = []

        # print(grid_list)

    for i in range(T):
        counter_area = {}
        contested = 0
        army = []
        armyLocX = []
        armyLocY = []
        for j in range(len(grid_list[i])):   #row
            for k in range(len(grid_list[i][j])):                    #column
                item = grid_list[i][j][k]
                if "#" != item and "." != item:
                    army.append(item)
                    armyLocX.append(k)
                    armyLocY.append(j)
        # print(army)
        # print(armyLocX)
        # print(armyLocY)
        distinct_army = list(set(army))
        distinct_army.sort()
        for zzz in distinct_army:
            counter_area[zzz]=0
        # print(counter_area)
        for l in range(len(army)):
            flag = False
            # print(grid_list[i])
            # print("{0} {1}".format(army[l], army.count(army[l])))
            first_item = grid_list[i][armyLocY[l]][armyLocX[l]]
            if first_item != "!":
                result = isConflicted(army=army[l], x_location=armyLocX[l], y_location=armyLocY[l], grid=grid_list[i],
                                      flag=flag)
                # print("Result Function: {}".format(result))
                # for y in range(len(grid_list[i])):
                #     for z in grid_list[i][y]:
                #         print(z, end='')
                #     print()
                if result:
                    contested += 1
                else:
                    counter_area[army[l]] += 1
        # print("Final Result: {}".format(contested))

    # Print the result
    # for i in range(T):
        print("Case {}:".format(i+1))
        for key, val in counter_area.items():
            if val != 0:
                print("{0} {1}".format(key, val))
        print("contested {}".format(contested))
