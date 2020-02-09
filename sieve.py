
import math
def sieve(n):
  primes = [True for i in range(n)]
  print(primes)
  primes[0] = primes[1] = False
  for i in range(2, round(math.sqrt(n))):
    if primes[i]:
      for j in range(0, n):
        if i*i + i*j >= n:
          break
        primes[i*i + i*j] = False
  return primes

