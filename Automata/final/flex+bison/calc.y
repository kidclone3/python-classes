%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

extern FILE *yyin;

void yyerror (char const *s);
int yylex();
void checkDiv(int num);
float divv(int num1, int num2);
int symbolVal(char symbol);
void updateSymbolVal(char symbol, int val);

int symbols[52];
int output = 0;
int waiting[2];
%}

%union {
    int num; char id;
}

%token NUMBER
%token VAR
%token EQUAL PLUS MINUS TIMES DIVIDE
%token NEWLINE

%type<num> NUMBER Declaration Expression OperandLeft OperandRight TERM
%type<id> VAR

%start Input
%%

Input:
	Declaration Declaration Declaration Expression { printf("%d\n",output); exit(0); }
;

OperandLeft:
    VAR {
        waiting[0] = symbolVal($1);
    }
    | NUMBER {
        waiting[0] = $1;
    }

OperandRight:
    VAR {
        waiting[1] = symbolVal($1);
    }
    | NUMBER {
        waiting[1] = $1;
    }

TERM:
	NUMBER
	| PLUS NUMBER {$$ = + $2}
	| MINUS NUMBER {$$ = - $2}

Declaration:
	VAR EQUAL TERM NEWLINE {
        updateSymbolVal($1,$3);
    }
;

Expression:
	OperandLeft PLUS OperandRight { 
        output = waiting[0] + waiting[1];
    }
	| OperandLeft MINUS OperandRight { 
        output = waiting[0] - waiting[1];
    }
	| OperandLeft TIMES OperandRight { 
        output = waiting[0] * waiting[1];
    }
	| OperandLeft DIVIDE OperandRight { 
        checkDiv(waiting[0]);
        divv(waiting[0], waiting[1]);
    }   
;

%%
float divv(int num1, int num2){
    printf("%f\n",num1*1.0/(num2*1.0));
    exit(0);
}

int computeSymbolIndex(char token)
{
	int idx = -1;
	if(islower(token)) {
		idx = token - 'a' + 26;
	} else if(isupper(token)) {
		idx = token - 'A';
	}
	return idx;
} 

int symbolVal(char symbol)
{
	int bucket = computeSymbolIndex(symbol);
	return symbols[bucket];
}
void updateSymbolVal(char symbol, int val)
{
	int bucket = computeSymbolIndex(symbol);
	symbols[bucket] = val;
}

void checkDiv(int num){
	if (!num){
		printf("Can not divide by zero\n");
		exit(1);
	}
}



void yyerror (char const *s) {
	fprintf (stderr, "%s\n", s);
}


int main(int argc, char* argv[]) {
	if (argc == 2){
		FILE *file = fopen(argv[1], "r");
		if(!file){
			fprintf(stderr, "Can not read file %s\n", argv[1]);
			exit(1);
		}else{
			yyin = file;
		}
	}
  if (yyparse())
     fprintf(stderr, "Successful parsing.\n");
  else
     fprintf(stderr, "error found.\n");
}