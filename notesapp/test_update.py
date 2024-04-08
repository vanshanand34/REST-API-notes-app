import requests

#testing note updation by passing required details to update the corresponding note object
login_url = "http://127.0.0.1:8000/notesapp/updatenoteapi"
credentials = {'token':'ae08b1078707d9d2127fff36205a94bbcf486a8d','id':27,'title':'fourth note', 'content':'changed fourth note','allowed_users':'anand@example.com,xyz@gmail.com,temp2@example.com'}

response = requests.post(login_url, data=credentials)
print(response)
# Check for successful updation in note 
if response.status_code == 201 or response.status_code==200:
    data = response.json()  # Assuming response is JSON
    print(f"Updated note successfully! Retrieved data: {data}")
else:
    print(f"Request failed! Status code: {response.status_code}")
