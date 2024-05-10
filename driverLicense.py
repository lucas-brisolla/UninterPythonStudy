DRIVER_LICENSE_AGE = 18
birth_year = int(input("Insert your birth year: "))
current_year = 2024
your_age = current_year - birth_year
if your_age >= DRIVER_LICENSE_AGE:
  print(f"Yeah! you're {your_age} years old! now you can get your driver's license! :D")
else:
  print(f":( you're {your_age} years old! you still can't get the driver's license!")