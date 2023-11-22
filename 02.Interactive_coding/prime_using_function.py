def prime(n):
  prime_list=[]
  for i in range(1,n+1):
    if n%i==0:
        prime_list.append(i)
  if len(prime_list)<=2:
      print(f"{n} is a prime number")
  else:
      print(f"{n} is not a prime number")

n = int(input("Enter a Number"))
prime(n)
