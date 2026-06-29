# Cyber Threat AI - Basic Phishing URL Detector
def check_url(url):
    # Common phishing indicators
    suspicious_keywords = ["login", "verify", "secure", "account", "update"]
    
    score = 0
    
    # Check for keywords
    for word in suspicious_keywords:
        if word in url.lower():
            score += 1
            
    # Check for suspicious character patterns
    if url.count('-') > 2:
        score += 1
        
    return "Phishing Detected" if score >= 2 else "Safe"

# Example Usage
target_url = "http://secure-login-verify-account.com"
print(f"Analyzing {target_url}...")
print(f"Result: {check_url(target_url)}")