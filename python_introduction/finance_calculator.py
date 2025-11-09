#Prompt
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#Monthly savings calculation
monthly_savings = monthly_income - monthly_expenses
#Annual savings calculation
rate = 0.05
time = 12
projected_savings = monthly_savings * time + (monthly_savings * time * rate)

#Output
print("Your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:",projected_savings)