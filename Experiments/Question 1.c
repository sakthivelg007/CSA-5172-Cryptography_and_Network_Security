#include <stdio.h>
#include <ctype.h>

int main() {
    char message[100];
    int key, i;

    printf("Enter a message to encrypt: ");
    fgets(message, 100, stdin);

    printf("Enter a key (1-25): ");
    scanf("%d", &key);

    // Encryption
    for (i = 0; message[i] != '\0'; i++) 
    {
        if (isalpha(message[i])) 
        {
            if (isupper(message[i])) 
            {
                message[i] = ((message[i] - 'A' + key) % 26) + 'A';
            } else 
            {
                message[i] = ((message[i] - 'a' + key) % 26) + 'a';
            }
        }
    }

    printf("Encrypted Message: %s\n", message);

    // Decryption
    for (i = 0; message[i] != '\0'; i++) 
    {
        if (isalpha(message[i])) 
        {
            if (isupper(message[i])) 
            {
                message[i] = ((message[i] - 'A' - key + 26) % 26) + 'A';
            } else 
            {
                message[i] = ((message[i] - 'a' - key + 26) % 26) + 'a';
            }
        }
    }

    printf("Decrypted Message: %s\n", message);

    return 0;
}
