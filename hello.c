#include <stdio.h>

int main() {
    // Define an array of character arrays (strings)
    char *users[] = {"User1", "User2", "User3"};

    // Calculate the number of elements in the array
    int numUsers = sizeof(users) / sizeof(users[0]);

    printf("C says: Hello, World!\n");

    // Loop through the array and print each user on a separate line
    for (int i = 0; i < numUsers; i++) {
        printf("%s\n", users[i]);
    }

    return 0;
}
