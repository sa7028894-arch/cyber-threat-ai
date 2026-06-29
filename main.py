import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

def check_threat_feed(url):
    headers = {"x-apikey": API_KEY}
    params = {'url': url}
    
    print(f"Submitting {url} to VirusTotal...")
    
    # Step 1: Submit URL
    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=params)
    
    if response.status_code == 200:
        analysis_id = response.json()['data']['id']
        print(f"Analysis ID received: {analysis_id}")
        
        # Wait a few seconds for the scan to process
        time.sleep(10)
        
        # Step 2: Get the final report
        print("Fetching final report...")
        report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        report_response = requests.get(report_url, headers=headers)
        
        return report_response.json()
    else:
        return {"error": f"Submission failed with code: {response.status_code}"}

# Run the analysis
result = check_threat_feed("http://google.com")
# ... (Keep all your existing code above) ...

# Final processing of the report
stats = result['data']['attributes']['last_analysis_stats']
malicious_count = stats.get('malicious', 0)

print("-" * 30)
if malicious_count > 0:
    print(f"ALERT: This URL is MALICIOUS! ({malicious_count} vendors flagged it.)")
else:
    print("STATUS: This URL is CLEAN.")
print("-" * 30)