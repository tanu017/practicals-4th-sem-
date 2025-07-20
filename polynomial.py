import time 
import math
def brute_force(coef, n, x):
  sum = 0.0
  for i in range(n+1):
    sum += coef[i] * math.pow(x, i)
  return sum

def hr(coef, n, x):
  result = coef[n] 
  for i in range(n-1, -1, -1):
    result = result * x + coef[i]
  return result 

n = int(input("Enter degree of polynomial: "))
coef = [0]*(n+1)
print("Enter the coefficients from highest degree to lowest degree: ")
for i in range(n, -1, -1):
  coef[i] = int(input())
x = float(input("Enter x: "))
start = time.time()
result_BF = brute_force(coef, n, x)
end = time.time()
time_used = end - start
print(f"Time taken in Brute force - {result_BF:.2f} = {time_used:.6f} milliseconds")

start = time.time()
result_HR = hr(coef, n, x)
end= time.time()
time_used = end - start
print(f"Time taken in HR - {result_HR:.2f} = {time_used:.6f} milliseconds")
