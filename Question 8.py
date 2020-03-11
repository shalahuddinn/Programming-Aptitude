def solution(A):
  arr = []
  maxValue = max(A)
  count = 0
  
  for in range(len(A)):
    arr.append(A[i])
    if (len(arr) == max(arr)):
      count += 1
  return count
