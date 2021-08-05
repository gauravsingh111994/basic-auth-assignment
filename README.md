# Role Based Access Control:

## Language:
**Python3**
## Installation:

```sh
pip3 install -r requirements.txt
python3 app.py
```
## Usage:

- After running app.py visit http://0.0.0.0:8889 or http://localhost:8889
- Login form will appear on the Frontend
- User the following credential for access

| Username | Password | Access |
| ------ | ------ | ------ |
| admin | admin | Read,write,delete |
| user1 | user1 | Read |
| user2 | user2 | Write |
| user3 | user3 | Delete |

- After successfull login UI will open with Read, Write, Delete and Logout button
- All the buttons will be clickable, and if you click the button and the user will have sufficient permission then "Operation of read/write/delete" will be displayed else "Access denied"
- If you try to access the url directly then also "Access denied" message will come up

## Code structure

- The code uses Flask framework
- Internally had implemented wrapper function to block the endpoint if unauthorized access happens
- Class had been implemented for returning User Access
- Json config had been made to map the API access

## Images

# Login Page
![Login](images/1.png?raw=true "Login page")

# Display Page
![Display](images/2.png?raw=true "Display page")

# Operation Allowed Page
![Operation](images/3.png?raw=true "Operation page")

# Access Denied Page
![access denied](images/4.png?raw=true "Access Denied page")

