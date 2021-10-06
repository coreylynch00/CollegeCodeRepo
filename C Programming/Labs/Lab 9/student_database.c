#include <stdio.h>
#include <stdlib.h>

struct student{
    char *name;
    int grade;
};

int change_grade(struct student *s, int new_grade){
    if (s==NULL) return 1;
    s->grade = new_grade;
    return 0;
}

int new_entry(struct student *array, int *length){
    // Task 4
    // checking if there is space in the DB
    if (*length>=20) return 1;
    // reading the name to a temp array to check the length of the name
    char temp[20];
    int j;
    printf("Add a new entry: ");
    scanf("%s", temp);
    for (j=0;temp[j]!='\0';j++);
    array[*length].name = malloc(j+1);
    for (j=0;temp[j]!='\0';j++){
        array[*length].name[j] = temp[j];
    }
    
    printf("Student grade: ");
    scanf("%d", &(array[*length].grade));
    getchar();
    
    *length = *length + 1;
    return 0;
}

struct student *return_index(struct student *array, int index){
    // Task 5
    if (index >= 20) return NULL;
    return &array[index];
}

void print_DB(struct student array[], int length){
    // Task 6 
    int i = 0;
    for (i=0;i<length;i++){
        printf("%d. %s -> %d%%\n", i, array[i].name, array[i].grade);
    }
}

struct student *get_lowest_index(struct student array[], int length){
    // Task 7
    int lowest_index = 0;
    int i;
    for (i=1;i<length;i++){
        if (array[i].grade < array[lowest_index].grade){
            lowest_index = i;
        }
    }
    return(&array[lowest_index]);
}

struct student *get_highest_index(struct student array[], int length){
    // Task 8
    int highest_index = 0;
    int i;
    for (i=0;i<length;i++){
        if (array[i].grade > array[highest_index].grade){
            highest_index = i;
        }
    }
    return(&array[highest_index]);
}

float get_average_grade(struct student *array, int length){
    // Task 9
    int sum = 0;
    int i = 0;
    for (i=0;i<length;i++){
        sum = sum + array[i].grade;
    }
    return (float)sum/length;
}

void histogram(struct student array[], int length){
    
    int bins[10];
    int i;
    for (i = 0;i<10;i++){
        bins[i] = 0;
    }
    
    for (i=0;i<length;i++){
        bins[array[i].grade/10]++;
    }
    
    int j;
    for (i=0;i<10;i++){
        printf("[%02d]:", i*10);
        for (j=0;j<bins[i];j++){
            printf("#");
        }
        printf("\n");
    }
}

int main()
{
    struct student array[20];
    int index, grade;
    int DB_length = 0;
    struct student *p;
    
    char option;
    while(1){
        printf("1. Print database\n2. Add student\n3. Change grade\n"
               "4. Get student with lowest grade\n5. Get student with highest grade\n"
               "6. Get average grade\n7. Histogram of grades\n8. Exit\n");
        option = getchar();
        getchar();
        switch (option){
            case '1': 
                print_DB(array, DB_length); break;
            case '2':
                new_entry(array, &DB_length); break;
            case '3':
                printf("Index of the student whose grade will be updated: ");
                scanf("%d", &index);
                p = return_index(array, index);
                printf("This is the student you selected %s -> %d\n", p->name, p->grade);
                printf("What is the updated grade: ");
                scanf("%d", &grade); getchar();
                change_grade(p, grade);
                break;
            case '4': 
                p = get_lowest_index(array, DB_length);
                printf("Lowest grade is %s -> %d%%\n", p->name, p->grade);
                break;
            case '5':
                p = get_highest_index(array, DB_length);
                printf("Highest grade is %s -> %d%%\n", p->name, p->grade);
                break;
            case '6':
                printf("Average grade is %.2f%%\n", get_average_grade(array, DB_length));
                break;
            case '7':
                histogram(array, DB_length); break;
            case '8':
                return 0;
            
        }
    }

    return 0;
}





