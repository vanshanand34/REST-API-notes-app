import requests

#testing deletion of a note and passing token for authorisation
login_url = "http://127.0.0.1:8000/notesapp/deletenoteapi"
credentials = {'token':'9f8d24541592c0f07a6abbe1181e090fa0cebbba','id':24}

response = requests.post(login_url, data=credentials)

# Check for successful login (adjust based on API response format)
if response.status_code == 201 or response.status_code==200:
    data = response.json()  # Assuming response is JSON
    print(f"Note deleted successfully! Retrieved data: {data}")
else:
    print(f"Task failed! Status code: {response.status_code}")
