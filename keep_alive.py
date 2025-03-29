import requests
import time

URL = "https://bugsentinelai-assistant-a6qpdea6szu6ufclcmt8hu.streamlit.app/"  

while True:
    try:
        response = requests.get(URL)
        print(f"Pinged {URL}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(600)  
