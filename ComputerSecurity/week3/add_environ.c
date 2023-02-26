#include <stdio.h>
extern char** environ;
void main(int argc, char* argv[], char* envp[]) {
    int i = 0; char *v[2]; char *new_env[3];
    if (argc < 2) return;

    v[0] = "HOME"; v[1] = argv[1];    
}