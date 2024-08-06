#include <stdio.h>
#include <math.h>
#include <stdbool.h>


double sum(double a, double b){
    return a + b;
}

double diff(double a, double b){
    return a - b;
}

double prod(double a, double b){
    return a * b;
}

double quo(double a, double b){
    return a / b;
}

int main()
{
    double a,b;
    
    printf("Enter a: ");
    scanf("%lf", &a);
    
    printf("Enter b: ");
    scanf("%lf", &b);
    
    
    printf("\nSum: %.3lf\n",sum(a,b));
    printf("Diff: %.3lf\n", diff(a, b));
    printf("Product: %.3lf\n", prod(a, b));
    printf("Quotient: %.3lf\n", quo(a, b));
    
    return 0;
}
