import requests

#testing user logout by passing the token obtained during login/register
login_url = "http://127.0.0.1:8000/notesapp/getnoteapi?token=4cc427939f9cb3cd7d665fbeb8d809b9ef4571f0&page=2"
credentials = {"token": "4cc427939f9cb3cd7d665fbeb8d809b9ef4571f0'"}


response = requests.get(login_url, data=credentials)

# Check for successful logout
if response.status_code == 200 or response.status_code == 201:
    data = response.json()  # Assuming response is JSON
    print(f"Logout successful! Retrieved data: {data}")
else:
    print(f"Logout failed! Status code: {response.status_code}")
