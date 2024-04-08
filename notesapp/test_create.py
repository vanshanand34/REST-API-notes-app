import requests

#testing note creation 
login_url = "http://127.0.0.1:8000/notesapp/createnoteapi"
credentials = {'token':'9f8d24541592c0f07a6abbe1181e090fa0cebbba','title':'fifth note', 'content':'my fifth note','allowed_users':'anand@example.com,xyz@gmail.com'}

response = requests.post(login_url, data=credentials)
print(response)
# Check for successful login (adjust based on API response format)
if response.status_code == 201:
    data = response.json()  # Assuming response is JSON
    print(f"Created note successfully! Retrieved data: {data}")
else:
    print(f"Task failed! Status code: {response.status_code}")
