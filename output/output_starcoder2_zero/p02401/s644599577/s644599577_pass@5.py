#include <stdio.h>
int main(void) {
  int a =0;
  char op[10] ;
  int b= 0;

  scanf("%d %s %d", &a, op ,&b);

  while (op [0] != '?') {
    if (op [0] == '+')
      printf ("%d\n", a+b );
    else if (op[0] == '-')
      printf ("%d\n", a-b );
    else if (op[0] == '*')
      printf ("%d\n", a*b );
    else if (op [0] == '/')
      printf ("%d\n", a/b );

    scanf("%d %s %d",&a , op ,&b);
  }


}