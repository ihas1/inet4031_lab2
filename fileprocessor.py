# fileprocessor.py

# Define the filename
filename = "fileprocessor.input"

# Open the file for reading
with open(filename, "r") as file:
    lines = file.readlines()

# Initialize an empty list to store user data
user_data = []

# Process each line of the file
for line in lines:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Skip lines starting with a hashtag (#)
    if line.startswith("#"):
        continue

    # Split the line into a list using ':' as the delimiter
    parts = line.split(":")
    
    # Ensure there are at least 4 parts (User, Password, UserID, GroupID)
    if len(parts) >= 4:
        user = parts[0]
        password = parts[1]
        userid = parts[2]
        groupid = parts[3]
        
        # Store user data as a dictionary
        user_data.append({
            "user": user,
            "password": password,
            "userid": userid,
            "groupid": groupid
        })

# Print the user data
print("Printing out User Data:")
for data in user_data:
    print(f"The user {data['user']} has a password of {data['password']} "
          f"and has userid {data['userid']} and groupid {data['groupid']}")

print("End of User Data")
