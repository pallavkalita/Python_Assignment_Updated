def load_accounts():
    accounts = {}
    with open('accounts.txt', 'r') as file:
        for line in file:
            account_number, balance = line.strip().split(',')
            accounts[account_number] = float(balance)
    return accounts

def transfer_funds(from_account, to_account, amount):
    accounts = load_accounts()

    # Check if the accounts are valid
    if from_account not in accounts or to_account not in accounts:
        raise ValueError("Error: One or both account numbers are invalid!")

    # Check if there are enough funds to transfer
    if accounts[from_account] < amount:
        raise ValueError("Error: Not enough funds in the source account!")

    # Perform the transfer
    accounts[from_account] -= amount
    accounts[to_account] += amount

    print(f"Successfully transferred {amount} from account {from_account} to account {to_account}.")
    print(f"New balance for {from_account}: {accounts[from_account]:.2f}")
    print(f"New balance for {to_account}: {accounts[to_account]:.2f}")

# Example usage
try:
    transfer_funds('2001', '2004', 300)
except ValueError as e:
    print(e)
