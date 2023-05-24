total = 0
order = []
sandwichOrdered = False
beverageOrdered = False
friesOrdered = False

sandwich = input("Pick a type of sandwhich,chicken,beef,or tofu.")

print(sandwich)
if sandwich == "chicken":
  order.append("chicken sandwich")
  total = 5.25
  sandwichOrdered = True
  
elif sandwich == "beef":
  order.append("beef sandwich")
  total = 6.25
  sandwichOrdered = True

elif sandwich == "tofu":
  order.appened("tofu sandwich")
  total = 5.75
sandwichOrdered = True

print(total) 
beverage = input("Do you want a drink? ")
if beverage == "yes":
  beverageOrdered = True
  
  beveragesize = input("Would you like a small for $1.00, medium for $1.75, or a large for $2.25?  ")
  print("You said", beveragesize, "drink.")

  if beveragesize == "small":
    order.append("small beverage")
    total = total + 1.00
  if beveragesize == "medium":
    order.append("medium beverage")
    total = total + 1.75
  if beveragesize == "large":
    order.append("large beverage")
    total = total + 2.25
beverage = True
print(total)
fries = input("Do you want french fries? ")
if fries == "yes":
  friesOrdered = True
   
  friesize = input("Would you like a small for $1.00, medium for $1.50, or large for $2.00  ")
  print("You said", friesize, "fries.")

  if friesize == "small":
    friesize = input("Would you like to mega-size your fries? ")
    if friesize == "yes":
      order.append("large fries")
      total = total + 2.00
    else:
      if friesize == "no":
        order.append("small fries")
        total = total + 1.00
  elif friesize == "medium":
    order.append("medium fries")
    total = total + 1.50 
  elif friesize == "large":
    order.append("large fries")
    total = total + 2.00
print(total)
ketchup = input("Do you want ketchup?(.25 each) ")

if ketchup == "yes":
  ketchupRequest = 15  # integer value of ketchup is ketchupRequest
  while ketchupRequest >= 11:
    ketchup = input("How many would you like?  Limit is 10: ")  # text or string value of ketchup is ketchup
    ketchupRequest = int(ketchup)
  total = total + (ketchupRequest * .25)
  order.append(ketchup +" Ketchup Packets")
print(total)
if (sandwichOrdered == True and beverageOrdered == True and friesOrdered == True):
  total = (total - 1)

print(total)
print("You ordered:  ")
for food in order:
  print("  - ", food)
print("Your total is: $", total)
