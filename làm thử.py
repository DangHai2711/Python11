a = int(input("nhập a: "))
b =int(input("nhập b: "))
def rutgonps(a,b):
    if a>b :
      for i in range(2, b+1):
       if a%i == 0 & b % i == 0:
         print(p = a/i)
         print(q = b/i)
    else:
      for i in range(2, a+1):
       if a%i == 0 & b % i == 0:
         print(p = a/i)
         print(q = b/i)
