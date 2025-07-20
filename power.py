def brute_force(a, n):
  result = 1
  for i in range(n):
    result *= a
  return result

def divide_conquer(a, n):
  if n==0:
    return 1
  elif n%2 == 0:
    return divide_conquer(a*a, n//2)
  else: 
    return a*divide_conquer(a*a, n//2)

a, n = map(int, input("Enter a and n: ").split())
print("Result using bruteforce: ", brute_force(a, n))
print("Result using divide_conquer: ", divide_conquer(a, n))
