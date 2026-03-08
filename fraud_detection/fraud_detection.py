def check_fraud(amount):
    if amount > 20000:
        print("⚠ ALERT: Suspicious transaction detected!")
        return True
    else:
        print("Transaction looks normal.")
        return False