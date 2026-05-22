'''
## Simulate a simple ATK transaction. Start with a balance of 5000. Ask the user for an option: 1.Withdraw 2. Deposit 3. Check balance
    - For withdraw, ask the amount. If amount > balance, print "Insufficient funds". Else deduct and show new balance.
    - For deposite, add amount and show new balance.
    - For check balance, just show balance.
    - If invalid option, print "Invalid choice".   
'''

transaction = int(input(
"1. Withdraw  \n" \
"2. Deposit  \n" \
"3. Check Balance  \n"
"Enter a choice : "))
balance = 5000

if transaction == 1 :
    amount = int(input("Enter the amount to withdraw : "))
    if amount > balance :
        print("Insufficient Funds....")
    else :
        balance = balance - amount
        print(balance)
elif transaction == 2 :
    new_amount = int(input("Enter the amount : "))
    if new_amount <= 0 :
        print("Enter the amount greater than Zero...")
    else :
        balance = balance + new_amount
        print(balance)
elif transaction == 3 :
    print(balance)
else :
    print("Invalid choice...")