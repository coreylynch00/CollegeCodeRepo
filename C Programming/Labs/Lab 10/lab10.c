#include <stdio.h>
#include <stdlib.h>

struct student{
    char name[10];
    int year;
};

struct list_node{
    int data_type;
    void *data; // void pointer!!!
    struct list_node *next;
};

enum {
    STUDENT,
    STRING,
    INT
};

struct student *new_student(){
    
    struct student *s; // pointer - holds addresses
    s = malloc(sizeof(struct student)); //returns a memory address
    printf("Student name: "); 
    scanf("%s", s->name);
    printf("Student year: "); 
    scanf("%d", &(s->year));
    getchar();
    return s;
}


struct list_node *new_node(struct student *data, int data_type){
    struct list_node *n;
    n = malloc(sizeof(struct list_node));
    n->data_type = data_type;
    n->data = data;
    n->next = NULL;
    return n;
}

void append(struct list_node *list_head, struct list_node *node){
    struct list_node *cursor;
    cursor = list_head;
    while (cursor->next != NULL){
        cursor = cursor->next;
    }
    cursor->next = node;
    node->next = NULL;
}

void add_after(struct list_node *n, struct list_node *node){
    struct list_node *next_node = n->next;
    n->next = node;
    node->next = next_node;
}

struct list_node *find_node(struct list_node *list_head, void *data){
    struct list_node *cursor;
    cursor = list_head;
    while (cursor->next != NULL){
        cursor = cursor->next;
        if (cursor->data == data){
            return cursor;
        }
    }
    return NULL;
}

struct list_node *find_node_by_index(struct list_node *list_head, int index){
    struct list_node *cursor;
    cursor = list_head;
    int i;
    if (i < 0){
        printf("Index must be positive.\n");
        return NULL;
    }
    for (i=0;i<index;i++){
        cursor = cursor->next;
        if (cursor->next == NULL){
            return NULL;
        }
    }
    return cursor;
}

void remove_func(struct list_node *list_head, struct list_node *n){
    struct list_node *cursor;
    cursor = list_head;
    while(cursor->next != n){
        cursor = cursor->next;
    }
    cursor->next = n->next;
    free(n);
}

int main()
{
    
    char input = 0;
    struct student *s;
    struct list_node *cursor;
    struct list_node *cursor_index;
    struct list_node list_head;
    list_head.data = NULL;
    int index;
    
    while (input != 'q'){
        printf("1. Print list\n");
        printf("2. Add value\n");
        printf("3. Insert value\n");
        printf("4. Remove value\n");
        
        input = getchar(); getchar();
        switch (input){
            case '1':
                cursor = &list_head;
                while (cursor->next != NULL){
                    cursor = cursor->next;
                    s = (struct student *)cursor->data;
                    printf("%s (%d)\n", s->name, s->year);
                }
                break;
            case '2':
                s = new_student();
                cursor = new_node(s, STUDENT);
                append(&list_head, cursor);
                break;
            case '3':
                printf("At what index do you want to insert a new node: ");
                scanf("%d", &index); getchar();
                cursor_index = find_node_by_index(&list_head, index);
                s = new_student();
                if (cursor_index != NULL){
                    cursor = new_node(s, STUDENT);
                    add_after(cursor_index, cursor);
                }
                break;
            case '4':
                printf("Index of the node you want to remove: ");
                scanf("%d", &index); getchar();
                cursor_index = find_node_by_index(&list_head, index);
                if (cursor_index != NULL){
                    remove_func(&list_head, cursor_index);
                }
                break;
        }
    }
    return 0;
}



