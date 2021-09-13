reservadas = {
    #'end'       :   'END',
    #'Nothing'   :   'NOTHING',
    #'Int64'     :   'INT64',
    #'Float64'   :   'FLOAT64',
    #'Bool'      :   'BOOL',
    #'Char'      :   'CHAR',
    #'String'    :   'STRING',
    #'struct'    :   'STRUCT',
    'log'       :   'LOG',
    'log10'     :   'LOG10',
    #'sin'       :   'SIN',
    #'cos'       :   'COS',
    #'tan'       :   'TAN',
    'sqrt'      :   'SQRT',
    'print'     :   'PRINT',
    'println'   :   'PRINTLN',
    #'local'     :   'LOCAL',
    #'function'  :   'FUNCTION',
    #'parse'     :   'PARSE',
    #'trunc'     :   'TRUNC',
    #'float'     :   'FLOAT',
    #'string'    :   'FSTRING',
    #'typeof'    :   'TYPEOF',
    #'push'      :   'PUSH',
    #'pop'       :   'POP',
    #'length'    :   'LENGTH',
    #'if'        :   'IF',
    #'elseif'    :   'ELSEIF',
    #'else'      :   'ELSE',
    #'while'     :   'WHILE',
    #'in'        :   'IN',
    #'break'     :   'BREAK',
    #'continue'  :   'CONTINUE',
    #'return'    :   'RETURN',
    #'mutable'   :   'MUTABLE',
    #'uppercase' :   'UPPERCASE',
    #'lowercase' :   'LOWERCASE',
    'true'      :   'TRUE',
    'false'     :   'FALSE',
}

tokens = [
    'PTCOMA',
    #'CORCHEA',
    #'CORCHEC',
    #'DDOSPT',
    'MAS',
    'POR',
    'ELEVADO',
    'MENOS',
    'DIVIDIDO',
    'MODULO',
    'PAREA',
    'PAREC',
    'MENOR',
    'MAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    #'IGUAL',
    'EQUALS',
    'DIFERENTE',
    'OR',
    'AND',
    'NOT',
    #'DOLAR',
    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENA',
    'CARACTER',
    'COMA',
] + list(reservadas.values())

# Tokens
t_PTCOMA        = r';'
#t_CORCHEA       = r'\['
#t_CORCHEC       = r'\]'
#t_DDOSPT        = r'::'
t_MAS           = r'\+'
t_POR           = r'\*'
t_ELEVADO       = r'\^'
t_MENOS         = r'\-'
t_DIVIDIDO      = r'/'
t_MODULO        = r'%'
t_PAREA         = r'\('
t_PAREC         = r'\)'
t_MENOR         = r'<'
t_MAYOR         = r'>'
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
#t_IGUAL         = r'='
t_EQUALS        = r'=='
t_DIFERENTE     = r'!='
t_OR            = r'\|\|'
t_AND           = r'&&'
t_NOT           = r'!'
#t_DOLAR         = r'\$'
t_COMA          = r','

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es demasiado grande (%d)", t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es demasiado grande (%d)", t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r'\'.?\''
    t.value = t.value[1:-1]
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])

from classes.Tipo import TYPE
from classes.Value import Value
from classes.Aritmetica import Aritmetica
from classes.Print import Print
from classes.Logica import Logica
from classes.Relacional import Relacional
import ply.lex as lex
lexer = lex.lex()

precedence = (
    #('right', 'IGUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'EQUALS', 'DIFERENTE'),
    ('left', 'MAYOR', 'MENOR', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('right', 'ELEVADO'),
)

def p_init(t):
    'init           :   instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones  : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones  :   instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion  : PRINT args sync 
                    | PRINTLN args sync
    '''
    if t[1] == 'print': t[0] = Print(t[2], TYPE.FPRINT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'println' : t[0] = Print(t[2], TYPE.FPRINTLN, t.lexer.lineno, t.lexer.lexpos)

def p_expl(t):
    '''expl         : expl OR expl
                    | expl AND expl
    '''
    if t[2] == '||': t[0] = Logica(t[1], t[3], TYPE.LOGICOR, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '&&': t[0] = Logica(t[1], t[3], TYPE.LOGICAND, t.lexer.lineno, t.lexer.lexpos)

def p_expl_expr(t):
    'expl           : expr'
    t[0] = t[1]

def p_expr(t):
    '''expr         : expr EQUALS expr
                    | expr DIFERENTE expr
                    | expr MENOR expr
                    | expr MAYOR expr
                    | expr MAYORIGUAL expr
                    | expr MENORIGUAL expr
    
    '''
    if t[2] == '==': t[0] = Relacional(t[1], t[3], TYPE.EQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '!=': t[0] = Relacional(t[1], t[3], TYPE.DIFFERENT, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '<=': t[0] = Relacional(t[1], t[3], TYPE.LOWEREQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '>=': t[0] = Relacional(t[1], t[3], TYPE.GREATEREQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '<': t[0] = Relacional(t[1], t[3], TYPE.LOWER, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '>': t[0] = Relacional(t[1], t[3], TYPE.GREATER, t.lexer.lineno, t.lexer.lexpos)

def p_expr_expm(t):
    'expr           : expm'
    t[0] = t[1]

def p_expm(t):
    '''expm         : expm MAS expm
                    | expm MENOS expm
                    | expm POR expm
                    | expm DIVIDIDO expm
                    | expm MODULO expm
                    | expm ELEVADO expm
    '''
    if t[2] == '+': t[0] = Aritmetica(t[1], t[3], TYPE.ADDITION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '-': t[0] = Aritmetica(t[1], t[3], TYPE.SUBSTRACTION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '*': t[0] = Aritmetica(t[1], t[3], TYPE.MULTIPLICATION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '/': t[0] = Aritmetica(t[1], t[3], TYPE.DIVISION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '%': t[0] = Aritmetica(t[1], t[3], TYPE.MODULUS, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '^': t[0] = Aritmetica(t[1], t[3], TYPE.POWER, t.lexer.lineno, t.lexer.lexpos)


def p_expm_val(t):
    'expm           : expval'
    t[0] = t[1]

def p_expval_not(t):
    'expval         : NOT expval'
    t[0] = Logica(t[1], None, TYPE.NOT, t.lexer.lineno, t.lexer.lexpos)

def p_expval_neg(t):
    'expval         : MENOS expval'
    t[0] = Aritmetica(Value(-1, TYPE.TYPEINT64, t.lexer.lineno, t.lexer.lexpos), t[2], TYPE.MULTIPLICATION, t.lexer.lineno, t.lexer.lexpos)

def p_expval_string(t):
    'expval         : CADENA'
    t[0] = Value(t[1], TYPE.TYPESTRING, t.lexer.lineno, t.lexer.lexpos)

def p_expval_char(t):
    'expval         : CARACTER'
    t[0] = Value(t[1], TYPE.TYPECHAR, t.lexer.lineno, t.lexer.lexpos)

def p_expval_bool(t):
    'expval         : booleano'
    t[0] = Value(t[1], TYPE.TYPEBOOL, t.lexer.lineno, t.lexer.lexpos)

def p_expval_int(t):
    'expval         : ENTERO'
    t[0] = Value(t[1], TYPE.TYPEINT64, t.lexer.lineno, t.lexer.lexpos)

def p_expval_float(t):
    'expval         : DECIMAL'
    t[0] = Value(t[1], TYPE.TYPEFLOAT64, t.lexer.lineno, t.lexer.lexpos)

def p_expval_nativa(t):
    'expval         : nativa'

def p_expval_id(t):
    'expval         : ID'

def p_expval_paren(t):
    'expval         : PAREA expl PAREC'
    t[0] = t[2]


def p_nativa(t):
    '''nativa       : LOG10 args
                    | LOG args
                    | SQRT args
    '''

def p_list_values(t):
    'list_values    : list_values COMA expl'
    t[1].append(t[2])
    t[0] = t[1]

def p_list_value(t):
    'list_values    : expl'
    t[0] = [t[1]]

def p_args(t):
    'args           : PAREA list_values PAREC'
    t[0] = t[2]

def p_booleano(t):
    '''booleano     : TRUE
                    | FALSE
    '''
    t[0] = t[1]

def p_sync(t):
    'sync           : PTCOMA'

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)