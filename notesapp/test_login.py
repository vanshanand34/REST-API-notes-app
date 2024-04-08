import requests

#testing user authentication login and getting corresponding notes in response
login_url = "http://127.0.0.1:8000/notesapp/loginapi?username=temp&password=temp_pass"
credentials = {}


response = requests.get(login_url)

# Check for successful login (adjust based on API response format)
if response.status_code == 200:
    data = response.json()  # Assuming response is JSON
    print(f"Login successful! Retrieved data: {data}")
else:
    print(f"Login failed! Status code: {response.status_code}")
