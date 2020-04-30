#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#By: Osvaldo Amorim
#----------------------------------------------------------------------------
def divisibleSumPairs(n, k, ar):
  soma = 0
  pares = 0
  i = 0
  j = i + 1

  while i < n -1:
    while j < n:
      soma = ar[i] + ar[j]
      if (soma % k == 0):
        pares += 1
        #print(ar[i], "+", ar[j], "= ", soma, "pares = ", pares)
        j += 1
      else:
        j += 1
    i += 1
    j = i + 1
  #print(pares)
  return pares