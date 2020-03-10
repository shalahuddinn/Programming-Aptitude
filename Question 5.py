# Source: https://stackoverflow.com/questions/55147629/debugging-binary-search
def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = int((low + high)/2);
        if array[mid] > value:
            return binary_search(array, value, low, mid-1)    # answer
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid

if __name__ == '__main__':
    array = []
    f = open("input5.in", "r")

    for i in range(10000):
        array.append(int(f.readline()))
    for i in range(10000):
        value = int(f.readline())
        answer = binary_search(array, value, 0, 9999)
        print("%d" % answer)
