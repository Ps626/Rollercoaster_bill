print("hello Welcome to the roller coster ride")
height = int(input("Whats your height in cm? "))
bill= 0
if height >= 120:
  print("You can ride the rollercoster.")
  age= int(input("Whats your age?"))  
  if age < 12:
   bill= 5 
   print("please pay $5 for child ticket.")
  elif age <= 18:
   bill= 7
   print("Please pay $7 grown ups.")
  elif age>=45 and age<=55:
   bill += 0
   print("you don't have to pay anthing")
  else:
   bill= 12   
   print("please pay $12 for udlts.")
  
  Wants_photo = input("Do you wants photo graphs y or n")
  if Wants_photo == "y":
    bill+= 3
  print(f"Your final bill is ${bill}")
else:
  print("Sorry you have  to grow taller before you can ride. ")    