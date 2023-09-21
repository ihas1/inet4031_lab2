#!/bin/bash

# Define an array of strings
mylist=("User1" "User2" "User3")

echo "Bash says: Hello, World!"

# Loop through the array and print each user on a separate line
for user in "${mylist[@]}"; do
    echo "$user"
done
