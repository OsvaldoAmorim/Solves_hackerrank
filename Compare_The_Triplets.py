  #https://www.hackerrank.com/challenges/compare-the-triplets/problem
  #by: Osvaldo Amorim
  #---------------------------------------------------------------------
  
  def compareTriplets(a, b):
  i = 0
  bob_score = 0 
  alice_score = 0

  while i < len(a):
    if b[i] > a[i]:
      bob_score += 1
      i += 1
    elif a[i] > b[i]:
      alice_score += 1
      i += 1
    else:
      i += 1
  score = [alice_score, bob_score]
  return score
