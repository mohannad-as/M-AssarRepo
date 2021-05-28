number = int(input("Enter A Decimal Number to Convert it into binary: "))
blist= []
while number != 0:
      remain = number % 2
      blist.append(remain) 
      number = number // 2
blist.reverse()
     
      
print("The equivalent binary number is: ")
print(*blist)
