import requests

#testing user registeration and getting corresponding token in response
login_url = "http://127.0.0.1:8000/notesapp/registerapi"
credentials = {"username": "temp3", "password": "temp_pass3","password2":"temp_pass3","email":"temp@example.com","first_name":"temp3","last_name":"name"}


response = requests.post(login_url, data=credentials)

# Check for successful registeration 
if response.status_code == 201:
    data = response.json()  # Assuming response is JSON
    print(f"Registeration successful! Retrieved data: {data}")
else:
    print(f"Registeration failed! Status code: {response.data}")
