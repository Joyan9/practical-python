# mortgage.py
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    total_months += 1

    # Apply interest to the principal
    principal = principal * (1 + rate / 12)
    
    # Determine the payment amount for this month
    monthly_payment = payment
    
    # Add extra payment if within the specified range
    if extra_payment_start_month <= total_months <= extra_payment_end_month:
        monthly_payment += extra_payment

    # Adjust payment if it would overpay the principal
    if monthly_payment > principal:
        monthly_payment = principal  # Pay only the remaining balance

    # Reduce the principal and add to the total paid
    principal -= monthly_payment
    total_paid += monthly_payment

    #print(total_months, round(total_paid, 2), round(principal, 2))

print(f'Total paid: {round(total_paid, 2)} in {total_months} months')
