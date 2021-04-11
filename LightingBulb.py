import math
def getPrimeFactors(n):
  arr = []
  if n%2 ==0:
    arr.append(2)
    n/=2
    while n%2 ==0:
      n/=2
  
  for i in range(3,math.sqrt(n)+1,2):
    if i%n==0:
      arr.append(i)
      n/=i
      while n%i == 0:
        n/=i
  if n>2:
    arr.append(n)
  return arr

def lightBulb(states, numbers):
  dic = {}
  for i in numbers:
    for j in getPrimeFactors(i):
      if j in dic:
        dic[j]+=1
      else:
        dic[j]=1
    
