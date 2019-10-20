#include <stdio.h>
#include <stdlib.h>

int main()

{
   char response[1000] = "Hello World!";
   FILE *file;

   file = fopen("response.txt", "w");
   fprintf(file,"%s", response);
   fclose(file);

   return 0
}
