#include <stdio.h>
#include <string.h>

typedef struct {
    char name[52];
    char id[10];
    int age;
    int grades[3];
    
} Student;

typedef struct {
    int x;
    int y;
} Point;

void printInfo(Student student);
 
int main()
{
    Student test;
    
    Point p1 = {5,10};
    Point p2 = {1,2};
    Point p3 = {3, 4};
    
    Point points[11];
    
    strcpy(test.name, "John Doe");
    strcpy(test.id, "1010101012");
    test.age = 24;
    test.grades[0] = 7;
    test.grades[1] = 8;
    test.grades[2] = 7;

    // printf("Name: %s\n", test.name);
    
    printInfo(test);
    
    printf("\n(%d, %d)", p1.x, p1.y);
    printf("\n(%d, %d)", p2.x, p2.y);
    printf("\n(%d, %d)", p3.x, p3.y);

    for (int i = 10; i >= 0; i--){
        points[i].x = i;
        points[i].y = 10 - i;
    }
    
    printf("\n(%d, %d)", points[3].x, points[3].y);

    return 0;
}

void printInfo(Student student){
        printf("\nID: %s\n", student.id);
        printf("Name: %s\n", student.name);
        printf("Age: %d\n", student.age);
        printf("Grades: ");
        for(int i = 0; i < sizeof(student.grades)/sizeof(student.grades[0]); i++){
            printf("%d ", student.grades[i]);
        }
    }
