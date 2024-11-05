Python

import requests

# 1. GET Request: Fetching data from a URL
url = "https://api.example.com/users"

response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response data
    print(response.json())
else:
    print(f"Error: {response.status_code}")

# 2. POST Request: Sending data to a server
url = "https://api.example.com/users"

payload = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

headers = {'Content-type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print("User created successfully!")
else:
    print(f"Error: {response.status_code}")

# 3. PUT Request: Updating existing data
url = "https://api.example.com/users/123"

payload = {
    "email": "updated.john.doe@example.com"
}

response = requests.put(url, json=payload)

if response.status_code == 200:
    print("User updated successfully!")
else:
    print(f"Error: {response.status_code}")

# 4. DELETE Request: Removing data
url = "https://api.example.com/users/123"

response = requests.delete(url)

if response.status_code == 204:
    print("User deleted successfully!")
else:
    print(f"Error: {response.status_code}")
