# Import the sys module
import sys

# Process redirected input line-by-line
for line in sys.stdin:
    # Process each line as needed (e.g., split it by ':' and perform actions)
    parts = line.strip().split(":")
    if len(parts) >= 4:
        user = parts[0]
        password = parts[1]
        userid = parts[2]
        groupid = parts[3]
        # Perform actions on the data as required
        print(f"The user {user} has a password of {password} "
              f"and has userid {userid} and groupid {groupid}")
