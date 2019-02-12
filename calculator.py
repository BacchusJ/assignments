def tip_calculator():
  bill= input("Enter your total: ")
  tip=input("Tip amount: ")
  tip_value=float(bill)*float(tip)*.01
  print(f"Your Total Amount is {tip_value}")

tip_calculator()
