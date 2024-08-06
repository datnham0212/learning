#include <stdio.h>
#include <string.h>

// int longestNameLength(){
//     char name[] = "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr";
//     printf("The name is: %s\n", name);
//     printf("With the length of %lu characters", strlen(name));
// }

int main()
{
    // longestNameLength();
    char name[52];
    printf("What's your name: ");
    fgets(name, sizeof(name), stdin);
    name[strlen(name) - 1] = '\0';
    
    int age;
    printf("How old are you: ");
    scanf("%d", &age);
    
    double money;
    printf("How much cash you've got: $");
    scanf("%lf", &money);
    
    printf("\nHello, my name is %s and I'm %d\n", name, age);
    printf("Currently, I've $%-2.lf in my pocket.", money);
    
    return 0;
}
