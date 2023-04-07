income = (int(input("Enter Your income(Baht) >>")))
vat = (int(input("Enter your vat(%) >>")))
tax = (income * vat) / 100
income2 = income - tax
print("Your Tax is", tax, "Baht")
print("Your income is",  income2, "Baht")
