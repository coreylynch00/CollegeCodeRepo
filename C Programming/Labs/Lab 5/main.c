//Corey Lynch - SD2-A

#include <stdio.h>

int main(){
    //Exercise 1

    int chmatrix[4][4];
    char input = 0;
    char user_char;
    int num_chars = 0;
    int col = 0;
    int row = 0;
    int i;
    
    printf("Please input a string of chars:\n");
    
    while (input != '\n'){
        input = getchar();
        if (input == '\n') 
        break;
        
        chmatrix[row][col] = input;
        col += 1;
        num_chars += 1;
        
        if (col == 4){
            row += 1;
            col = 0;
            if (row == 4){
                while (input != '\n'){
                    input = getchar();
                }
                break;
            }
        }
    }
    
    for (i = num_chars; i < 16; i++){
        chmatrix[row][col] = '#';
        col += 1;
        if (col == 4){
            row += 1;
            col = 0;
            if (row == 4){
                break;
            }
        }
    }
    
    for (row = 0; row < 4; row++){
        for (col = 0; col < 4; col++){
            printf("%c ", chmatrix[row][col]);
        }
        printf("\n");
    }


    //Exercise 2 - searching through array
    printf("Enter a character you would like to search for in the string:\n");
    input = getchar();
    //printf("%c", input);
    getchar();
    
    for (row = 0; row < 4; row++){
        for (col = 0; col < 4; col++){
            if (input == chmatrix[row][col]){
                printf("(%d, %d)\n", row, col);
            }
        }
    }
    
    //Exercise 3 - printing a 2D sub-array of chars
    printf("Input row coordinate:\n");
    scanf("%d", &row);
    
    printf("Input column coordinate:\n");
    scanf("%d", &col);
    
    if (col < 0 || col >= 4){
        printf("Your column value is out of bounds!");
        return 1;
    }
    else if (row < 0 || row >= 4){
        printf("Your row value is out of bounds!");
        return 1;
    }
    
    if (row == 0){
        if (col == 0){
            printf("%c\n", chmatrix[row][col]);
        }
        else {
            printf("%c %c\n", chmatrix[row][col-1], chmatrix[row][col]);
        }
    }
    else {
        if (col == 0){
            printf("%c \n%c", chmatrix[row-1][col], chmatrix[row][col]);
        }
        else{
            printf("%c %c\n", chmatrix[row-1][col-1], chmatrix[row-1][col]);
            printf("%c %c\n", chmatrix[row][col-1], chmatrix[row][col]);
        }
    }
    
    return 0;
}






