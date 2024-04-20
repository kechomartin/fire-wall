# Import necessary libraries
import time

# Define a function to simulate the firewall with a 100ms delay
def firewall_login(username, password):
    # Simulate firewall processing delay
    time.sleep(0.1)  # 100ms delay
    
    # Check username and password against allowed credentials
    allowed_users = {"user1": "password1", "user2": "password2"}  # Example allowed credentials
    if username in allowed_users and allowed_users[username] == password:
        return True  # Login successful
    else:
        return False  # Login failed

# Example usage
username_input = input("Enter username: ")
password_input = input("Enter password: ")

if firewall_login(username_input, password_input):
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")
