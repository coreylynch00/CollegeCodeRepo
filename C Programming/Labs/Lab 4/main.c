
#include <stdio.h>

int main()
{
    
    //Exercise 1
    int num1 = 1;
    int num2 = 3;
    char char1 = 'a';
    
    int* pAddress1 = NULL;
    pAddress1 = &num1;
    printf("\n The location of num1 is at 0x%p", pAddress1);
    
    int* pAddress2 = NULL;
    pAddress2 = &num2;
    printf("\n The location of num2 is at 0x%p", pAddress2);
    
    char* pAddress3 = NULL;
    pAddress3 = &char1;
    printf("\n The location of char1 is at 0x%p\n", pAddress3);
    
    
    //Exercise 2
    printf("\nInt Value at address %p is %d", pAddress1, *pAddress1);
    printf("\nInt Value at address %p is %d", pAddress2, *pAddress2);
    printf("\nInt Value at address %p is %c\n", pAddress3, *pAddress3);
    
    //Exercise 3 (i)
    int testInt;
    printf("\nEnter an int:");
    scanf("%d", &testInt);
    printf("Number = %d\n", testInt);
    
    //Exercise 3 (ii)
    int phoneNumber;
    printf("\nEnter a phone number:");
    scanf("%010d", &phoneNumber);
    printf("Phone number = %010d\n", phoneNumber);
    
    char name[10];
    printf("\nEnter a name:");
    scanf("%s", name);
    printf("Name = %s\n", name);
    
    return 0;
}

