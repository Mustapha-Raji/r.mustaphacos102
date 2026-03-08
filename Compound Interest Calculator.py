principal = int(input("P($): "))
rate = int(input("R(%): "))/100
number_of_years = int(input("N: "))
time = int(input("T: "))

calc1 = 1 + (rate / number_of_years)
calc2 = calc1 ** (number_of_years * time)
calc3 = principal * calc2
print(f"Amount: {calc3}")
