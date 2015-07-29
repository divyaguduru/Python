print(Using Calculator)

def add(a,b)
   return (float(a)+float(b))
def sub(a,b)
   return (float(a)-float(b))
def mul(a,b)
   return (float(a)float(b))
def div(a,b)
   return (float(a)float(b))

calculator=1
choice=0
while calculator==1
   choice=input(enter choice)
   if choice=='1'
      print(hi)
      ch=add(input(num1),input(num2))
      print(ch)
   if choice=='2'
      print(hi)
      ch=sub(input(num1),input(num2))
      print(ch)
   if choice=='3'
      print(hi)
      ch=mul(input(num1),input(num2))
      print(ch)
   if choice=='4'
      print(hi)
      ch=div(input(num1),input(num2))
      print(ch)
   if choice=='5'
      print(end)
      calculator=0
