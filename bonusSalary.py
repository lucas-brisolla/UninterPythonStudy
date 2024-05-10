current_salary = float(input("Type the value of your salary: "))
years_employee = int(input("How long have you worked here: "))
bonus1 = 20 / 100
bonus2 = 10 / 100
if years_employee > 5:
  current_salary += current_salary * bonus1
  print(f"Congrats! you've been there for {years_employee} years, so you will recive a bonus of 20% in your salary! ${current_salary}")
else:
  current_salary += current_salary * bonus2
  print(f"You've been there for {years_employee} years, you will recive a bonus of 10% in your salary! ${current_salary}")
