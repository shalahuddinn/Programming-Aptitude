def solution(N):
  numOfDigit = 0

  resultOfPower = 11**N
  n = resultOfPower

  answer=0

  #Calculate the number of digit
  while(n!=0):
    n = n // 10
    numOfDigit+=1

  #Calculate the number of digit 1
  for i in range(numOfDigit-1, -1, -1):
    divider = 10**i
    currentDigit = (resultOfPower // divider)%10
    if (currentDigit==1):
      answer+=1

  return answer
