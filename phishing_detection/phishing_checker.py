def check_phishing(url):

    suspicious_keywords = ["login-bank", "verify-account", "secure-update"]

    for word in suspicious_keywords:
        if word in url:
            print("⚠ WARNING: This link may be a phishing attempt!")
            return True

    print("Link appears safe.")
    return False