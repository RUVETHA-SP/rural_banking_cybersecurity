
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from authentication.login_system import login
from fraud_detection.fraud_detection import check_fraud
from phishing_detection.phishing_checker import check_phishing
from monitoring.security_dashboard import log_security_event

balance = 50000


def banking_system():
    global balance

    if not login():
        return

    while True:
        print("\n----- Rural Digital Banking -----")
        print("1. Check Balance")
        print("2. Transfer Money")
        print("3. Check Link for Phishing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to transfer: "))

            if amount > balance:
                print("Insufficient balance")
                continue

            if check_fraud(amount):
                log_security_event("Fraudulent transaction attempt detected")

            balance -= amount
            print("✅ Transaction Successful")
            print("Remaining Balance:", balance)

        elif choice == "3":
            url = input("Enter link to check: ")
            if check_phishing(url):
                log_security_event("Phishing link detected")

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


banking_system()