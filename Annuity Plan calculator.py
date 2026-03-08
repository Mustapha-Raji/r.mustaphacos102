rate = float(input("R(%): "))/100
number_of_years = float(input("N: "))
time = float(input("T: "))
pmt = float(input("PMT: "))

calc1 = 1 + (rate / number_of_years)
calc2 = calc1 ** (number_of_years * time)
calc3 = calc2 - 1
calc4 = calc3 / (rate / number_of_years)
calc5 = calc4 * pmt

print(f"Amount: {calc5}")
