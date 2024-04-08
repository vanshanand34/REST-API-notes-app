import requests

#testing user authentication login and getting corresponding notes in response
login_url = "http://127.0.0.1:8000/notesapp/logoutapi"
credentials = {"token": "ae08b1078707d9d2127fff36205a94bbcf486a8d"}


response = requests.post(login_url, data=credentials)

# Check for successful login (adjust based on API response format)
if response.status_code == 200:
    data = response.json()  # Assuming response is JSON
    print(f"Login successful! Retrieved data: {data}")
else:
    print(f"Login failed! Status code: {response.status_code}")
