/* file: calc.y
 * date: 6/9/14
 * author: David Weinman
 *
 * description:
 *
*/

%{
#define MAXNUM 999999999999999
#define YYSTYPE double
#define YYINITDEPTH 500
#define YYMAXDEPTH 49
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int yylex (void);
void yyerror (char const *);
char numbuf[40];
%}

%token NUM

%left '-'
%left '+'
%left '/'
%left '*'
%left '^'
%left NUM

%% /* Grammer rules and semantics */

input:
    %empty
| input line
;

line: '\n'
| exp '\n'     { printf("=> %.10g\n\n", $1); }
;

exp: fac       { $$ = $1; } 
| exp '-' exp  { $$ = $1 - $3;             }
| exp '+' exp  { $$ = $1 + $3;             }
| exp '/' exp  { $$ = $1 / $3;             }
| exp '*' exp  { $$ = $1 * $3;             }
| exp '^' exp  { $$ = pow($1, $3);         }
;

fac:  NUM      { memset(numbuf, '\0', 40); snprintf(numbuf, 40, "%.16g", $1); if ($1 <= MAXNUM && (strlen(numbuf) < 17)) { $$ = $1; } else { yyerror("INVALID NUMERICAL LENGTH, MAX LENGTH IS 15"); exit(1); } };

%%

/* Here's a lexer */

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
# define MAXOPCT 50

static int op_ctr = 0;

int yylex() {

    int c;

    /* Skip white space */
    while ((c = getchar()) == ' ' || c == '\t')
        continue;
    /* Gather numbers. */
    if (c == '.' || isdigit(c)) {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUM;
    }
    /* Return eof */
    if (c == EOF)
        return 0;
    if (op_ctr > MAXOPCT) {
        yyerror("[!!] too many ops.\n");
        exit(1);
    }
    /* Return single char */
    ++op_ctr;
    return c;

}

int main(void) {
    printf("Enter an expression (MAX NUMBER LENGTH : 15, MAX OP COUNT : 50) (+, -, *, / or ^):\n");
    return yyparse();
}

/* Called by yyparse on error. */

void yyerror(char const *s) {
    fprintf(stderr, "%s\n", s);
}

