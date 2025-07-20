def factorial(n): 
  fact = 1
  for i in range(2, n+1):
    fact *= i
  return fact

def brute_force(n, k):
  return factorial(n)//(factorial(k)*factorial(n-k))

def DP(n, k):
  c = [[0 for j in range(k+1)] for i in range(n+1)]
  for i in range(n+1):
    for j in range(min(i, k)+1):
      if j==0 or j==i:
        c[i][j] = 1
      else: 
        c[i][j] = c[i-1][j-1] + c[i-1][j]
  return c[n][k]

n = int(input("Enter n: "))
k = int(input("Enter k: "))
print("Result in brute force: ", brute_force(n, k))
print("Result in DP: ", DP(n, k))
