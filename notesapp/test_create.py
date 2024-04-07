import requests

#testing user authentication login and getting corresponding notes in response
login_url = "http://127.0.0.1:8000/notesapp/createnoteapi"
credentials = {"title": "first", "content": "my first note","allowed_users":"xyz@gmail.com,temp@example.com"}
headers = {"Authorization" : "Token 9f8d24541592c0f07a6abbe1181e090fa0cebbba"}

response = requests.post(login_url, data=credentials)
print(response)
# Check for successful login (adjust based on API response format)
if response.status_code == 200:
    data = response.json()  # Assuming response is JSON
    print(f"Login successful! Retrieved data: {data}")
else:
    print(f"Login failed! Status code: {response.status_code}")
