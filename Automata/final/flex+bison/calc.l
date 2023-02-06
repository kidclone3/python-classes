%option noyywrap
%{
#include "calc.tab.h"
#include <stdlib.h>
#include <stdio.h>
%}
newline [\n]
whitespace [ \t]+
variable [a-zA-Z]
integer 0|[-]*[1-9][0-9]*

%%
{newline} {return NEWLINE;}
{whitespace} 
{variable} {yylval.id = yytext[0]; return VAR;}
{integer} { yylval.num=atoi(yytext); return NUMBER;}
"=" {return EQUAL;}
"+" {return PLUS;}
"-" {return MINUS;}
"*" {return TIMES;}
"/" {return DIVIDE;}
. {printf("Cannot understand character \n"); exit(1);}
%%