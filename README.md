# Programming-Aptitude
Several online coding test from various sources.

## Question 1
Some people have been studying the following problem: given two numbers, A and B, how many numbers from A to B, inclusive, are divisible by another number K. For example, if A is 1, B is 10, and K is 3, then there are 3 numbers that satisfy this: 3, 6, and 9. Help them by programming a solution to this problem!

Input:
The first line is the number of test cases T. Each test case has three numbers A, B, K, each on their own line given in that order.

Output:
For each test case, output one line of the form “Case C: X” (without the quotes), where C is the case number (starting from 1), and X is the number of integers between A and B, inclusive, that are divisible by K.

Constraints:
```json
1 ≤ T ≤ 100
1 ≤ A ≤ B < 10000
1 ≤ K < 10000
```

Sample Input:
```json
2
1
10
3
8
20
4 
```

Sample Output:
```json
Case 1: 3
Case 2: 4
```
## Question 2

There is a well-known puzzle called Word Search that involves looking for words in a grid of letters.The words are given in a list and can appear in the grid horizontally, vertically, or diagonally in any direction.In this task, you should implement a solver for word search.You will be given grids and a word to search for, and you have to find how many times that word comes out in the grid.Words that are spelled the same backwards and forwards, also known as palindromes, will not be given, so you don’t need to worry about words that match in the exact same spot in two different directions.

Input:
The first line is the number of test cases T. Each test case will have two numbers N and M, each on their own line given in that order.Following that is N lines of M lowercase letters each representing the grid of letters.Lastly, a word W is given that you must look for.

Output:
For each test case, output one line of the form “Case C: X” (without the quotes), where C is the case number (starting from 1), and X is how many times the word W appeared in the grid.

Constraints:
```json
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ M ≤ 100
1 ≤ length(W) ≤ 100
```

Sample Input:
```json
3
3
4
catt
aata
tatc
cat
5
5
gogog
ooooo
godog
ooooo
gogog
dog
2
8
bananana
kalibrrr
nana
```

Sample Output :
```json
Case 1: 4
Case 2: 8
Case 3: 4
```

## Question 3
You are presented with a map of a kingdom. Empty land on this map is depicted as ‘.’ (without the quotes), and mountains are depicted by ‘#’. This kingdom has factions whose armies are represented by lowercase letters in the map. Two armies of the same letter belong to the same faction.

Armies can go up, down, left, and right, but cannot travel through mountains. A region is an area enclosed by mountains. From this it can be deduced that armies cannot travel between different regions. A region is said to be controlled by a faction if it’s the only faction with an army in that region. If there are at least two armies from different factions in a region, then that region is said to be contested. Your task is to determine how many regions each faction controls and how many contested regions there are.

Input:
The first line is the number of test cases T. Each test case will have two numbers N and M, each on their own line given in that order. Following that is N lines of M characters that represent the map.

Output:
For each test case, output one line of the form “Case C:” (without the quotes), where C is the case number (starting from 1). On the following lines, output the factions that appear in the grid in alphabetical order if the faction controls at least one region and how many regions that letter controls. Factions that don’t control any regions should not be in the output. After this, print one last line of the form “contested K” where K is the number of regions that contain at least two distinct letters.

See the sample output below for details.

Constraints:
```json
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ M ≤ 100
```

Sample Input:
```json
2
2
2
.#
#a
12
15
###########....
#.......c.###..
####......#.#..
.#.########.#..
##...#..b#..#..
#.a.#...#...###
####.#.#d###..#
......#...e#xx#
.#....#########
.#.x..#..#.....
.######.c#.....
......####.....
```

Sample Output:
```json
Case 1:
a 1
contested 0
Case 2:
a 1
b 1
c 2
x 2
contested 1
```


## Question 4
The code should print the number from 1 to 100 including both ends, one per line, except it prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5, and "FizzBuzz" when the number is divisible by 3 and 5. Something is wrong with it. **Find and Fix it by modifying one line!**

```python
for i in xrange(1,100):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
```

## Question 5
The binary search algorithm allows you to find the position of a specific value in a sorted array of data very quickly. It works by checking the middle of that array. If the middle is smaller than the value we're looking for, then we can be sure that the value we're looking for must be in the larger half of the array. Otherwise it's in the smaller half. We can repeatedly apply that idea, with each repetition cutting away half of the items we're looking through. Below is an implementation of binary search, but something is wrong with it. **Find it and fix it by modifying one line!**

Input:
The input consists of the sorted array of length 10,000, followed by 10,000 queries. Each integer is given in its own line (there are 20,000 lines in total).

It is guaranteed that there are no duplicates in the array.

Output:
For every query value, output one line of output containing a single integer: the index that matches the query value, or -1 if the value is not in the array.

```python
def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = int((low + high)/2);
        if array[mid] > value:
            return binary_search(array, value, low, mid)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid


    array = []
    for i in range(10000):
        array.append(input())
    for i in range(10000):
        value = input()
        answer = binary_search(array, value, 0, 9999)
        print("%d" % answer)
```


## Question 6
This code prints all the permutations of the string lexicographically. Something is wrong with it. **Find and fix it by modifying or adding one line!**

Input:
The input consists of a single line containing a string of lowercase characters with no spaces in between. Its length is at most 7 characters, and its characters are sorted lexicographically.

Output:
All permutations of the string printed one in each line, listed lexicographically.

Sample Input:
```json
abc
```

Sample Output:
```json
abc
acb
bac
bca
cab
cba
```
```python
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
                running.pop()

raw = input()
characters = list(raw)
running = []
bitmask = 0
permutations()
```
