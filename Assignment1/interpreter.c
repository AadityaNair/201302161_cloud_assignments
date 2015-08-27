/*
    Interpreter
    Author: Aaditya M Nair
    Created On: Thu Aug 27 12:19:10 IST 2015

    Converts x86 to x64 assembly.
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc < 2)
    {
        printf("Filename not specified.\n");
        exit(-1);
    }
    printf("; x64 is backward compatible with x86\n; *without* any performance loss.\n");
    printf("; So here is the same code back at you.\n\n");

    printf("; 64-bit code for %s\n", argv[1]);

    int fp = fopen(argv[1], "r");
    if (fp == 0){
        printf("File not found.\n");
        exit(-2);
    }

    char buf[1000];
    while (fgets(buf,1000, fp)!=NULL)
                printf("%s",buf);
    return 0;
}
