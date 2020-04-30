#https://www.hackerrank.com/challenges/diagonal-difference/problem
#By: Osvaldo Amorim
#_________________________________________________________________
def diagonalDifference(arr):
    # Write your code here
  n = len(arr)
  count = 0
  j = n - 1
  diagonalP = 0
  diagonalS = 0
  
  while count < n:
    diagonalP += arr[count][count]
    #print("elemento é ", arr[count][count])
    #print("DP = ", diagonalP)
   
    diagonalS += arr[count][j]
    #print("elemento é ", arr[count][j])
    #print("DS = ", diagonalS)
    #print("")
    count += 1
    j = j -1
  difference = abs(diagonalP - diagonalS)

  return difference
