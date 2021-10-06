#include <stdio.h>
#include <stdlib.h>

/*Exercise 1 (i)
int sum_array(int *array, int length){
    int i, sum;
    
    for (i=0,sum=0;i<length;i++){
        sum+=array[i];
    }
    return sum;
}

void main(void){
    
    int sum;
    int array[] = {10,20,30,11,21,31};
    sum = sum_array(array, 6);
    //print sum
    printf("Sum = %d\n", sum);
}*/

/*Exercise 1 (ii)
int sum_array(int *array, int length){
    int i, sum;
    sum = 0;
    
    for(i=0;i<length;i++){
        scanf("%d", &array[i]);
    }
    
    for (i=0;i<length;i++){
        sum += array[i];
    }
    return sum;
}

int main(){
    int sum;
    int array[7];
    sum = sum_array(array, 7);
    printf("%d", sum);
    
    return 0;
}*/

/*Exercise 1 (iii)
int sum_array(){
    int i, sum, length;
    sum = 0;
    
    printf("How many integers? ");
    scanf("%d", &length);
    
    int *array;
    array = malloc(sizeof(int)*length);
    
    for (i=0;i<length;i++){
        scanf("%d", &array[i]);
    }
    
    for (i=0;i<length;i++){
        sum+=array[i];
    }
    return sum;
}

int main(){
    int sum;
    sum = sum_array();
    printf("%d", sum);
    
    return 0;
}*/

/*Exercise 2
int read_text(char *array){
    
    int length = 0;
    char input;
    int i =0;
    
    while(1){
        
        input = getchar();
        if (input == '\n') 
        break;
        
        array[i] = input;
        i+=1;
        length+=1;
    }
    array[i] = '\n';
    
    return length;
}

int main(){
    char charray[50];
    int length;
    length = read_text(charray);
    printf("%s \n", charray);
    printf("The length of the string is %d \n", length);
    
    return 0;
}*/
//Exercise 3









