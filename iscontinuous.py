def continuous(i):
  n = float(input("Enter a number: "))
  m = float(input("Enter another number: "))
  l = float(input("Enter an integer: "))
  r = float(input("Enter a number: "))
  if n!=l and m!=r:
      fx=(n*i)+m
      gx=(l*i)+r
      if fx==gx:
         return "function is continuous for the value of x=1"
      else:
         return "function isnt continuous for x=1"
  else:
     return "error"
print(continuous(1))


