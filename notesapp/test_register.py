import requests

#testing user authentication login and getting corresponding notes in response
login_url = "http://127.0.0.1:8000/notesapp/registerapi"
credentials = {"username": "temp", "password": "temp_pass","password2":"temp_pass","email":"xyz@example.com","first_name":"temp","last_name":"name"}


response = requests.post(login_url, data=credentials)

# Check for successful login (adjust based on API response format)
if response.status_code == 201:
    data = response.json()  # Assuming response is JSON
    print(f"Login successful! Retrieved data: {data}")
else:
    print(f"Login failed! Status code: {response.data}")
