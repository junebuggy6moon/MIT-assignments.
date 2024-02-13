
annual_salary = int(input("What is your annual salary: ")) #5.
percentage_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("The cost of your dream home: ")) #1

portion_down_payment = 0.25 * total_cost #250k #2.
current_savings = 0
monthly_salary = annual_salary/12

r = 0.04 # 3.annual return rate
number_of_months = 0
portion_saved = percentage_saved * monthly_salary #6

while current_savings <= portion_down_payment:
    monthly_investment = (current_savings * r) / 12  # 4.
    number_of_months += 1
    current_savings += monthly_investment + portion_saved #7

print(f"It will take you {number_of_months} months to save up for the down payment.")
