#include <stdio.h>
#include "example.h"

/* File : example.c */
double My_variable = 3.0;
struct Test a = { 1, NULL} ;

/* Compute factorial of n */
int fact(int n) {
   if (n <= 1) return 1;
   else return n*fact(n-1);
}

/* Compute n mod m */
int my_mod(int n, int m) {
   return(n % m);
}

int my_array(int arr[2]){
   printf("%d", arr[0]);
   return 0;
}

int my_ptr(int *a){
   printf("%d", *a);
   return 0;
}
