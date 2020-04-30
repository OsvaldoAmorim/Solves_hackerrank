#https://www.hackerrank.com/challenges/a-very-big-sum/problem
#by: Osvaldo Amorim
#--------------------------------------------------------------------------------
def aVeryBigSum(ar):
  n = len(ar)
  soma = ar[0]
  count = 1

  while count < n:
    soma = soma + ar[count]
    count += 1
  return soma
