from asyncore import loop


total_cost = float(input("How much does your dream home cost? "))
portion_down_payment = (total_cost*0.25)
current_savings = 0
r = 0.04
monthlyR = (current_savings*r/12)
annual_salary = float(input("How much do you earn annually? "))
portion_saved = float(input("How much do you want to save in percents? "))
monthly_savings = monthlyR+(annual_salary*(portion_saved*0.01)/12)

loops = 0

while current_savings <= portion_down_payment:
    current_savings += monthly_savings
    loops += 1

current_savings -= portion_down_payment

loops2 = loops

while current_savings < (total_cost - portion_down_payment):
    current_savings += monthly_savings
    loops2 += 1

print("  It will take", loops, "months until you have your Downpayment and", loops2, "months to completely pay it off")