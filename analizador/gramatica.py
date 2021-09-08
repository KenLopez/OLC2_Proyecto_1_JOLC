reservadas = {
    'end'       :   'END',
    'Nothing'   :   'NOTHING',
    'Int64'     :   'INT64',
    'Float64'   :   'FLOAT64',
    'Bool'      :   'BOOL',
    'Char'      :   'CHAR',
    'String'    :   'STRING',
    'struct'    :   'STRUCT',
    'log'       :   'LOG',
    'log10'     :   'LOG10',
    'sin'       :   'SIN',
    'cos'       :   'COS',
    'tan'       :   'TAN',
    'sqrt'      :   'SQRT',
    'print'     :   'PRINT',
    'println'   :   'PRINTLN',
    'local'     :   'LOCAL',
    'function'  :   'FUNCTION',
    'parse'     :   'PARSE',
    'trunc'     :   'TRUNC',
    'float'     :   'FLOAT',
    'string'    :   'FSTRING',
    'typeof'    :   'TYPEOF',
    'push'      :   'PUSH',
    'pop'       :   'POP',
    'length'    :   'LENGTH',
    'if'        :   'IF',
    'elseif'    :   'ELSEIF',
    'else'      :   'ELSE',
    'while'     :   'WHILE',
    'in'        :   'IN',
    'break'     :   'BREAK',
    'continue'  :   'CONTINUE',
    'return'    :   'RETURN',
    'mutable'   :   'MUTABLE',
    'uppercase' :   'UPPERCASE',
    'lowercase' :   'LOWERCASE',
    'true'      :   'TRUE',
    'false'     :   'FALSE',
}

tokens = [
    'PTCOMA',
    'CORCHEA',
    'CORCHEC',
    'DDOSPT',
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
    'IGUAL',
    'EQUALS',
    'DIFERENTE',
    'OR',
    'AND',
    'NOT',
    'DOLAR',
    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENA',
    'CARACTER',
    'COMA',
] + list(reservadas.values())

# Tokens
t_PTCOMA        = r';'
t_CORCHEA       = r'\['
t_CORCHEC       = r'\]'
t_DDOSPT        = r'::'
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
t_IGUAL         = r'='
t_EQUALS        = r'=='
t_DIFERENTE     = r'!='
t_OR            = r'\|\|'
t_AND           = r'&&'
t_NOT           = r'!'
t_DOLAR         = r'\$'
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
    print("Caracter no reconocido '$s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('right', 'IGUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'EQUALS', 'DIFERENTE'),
    ('left', 'MAYOR', 'MENOR', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MODULO'),
    ('right', 'ELEVADO'),
    ('left', 'PAREA', 'PAREC', 'CORCHEA', 'CORCHEC')
)

def p_init(t):
    'init           :   instrucciones'

def p_instrucciones(t):
    '''instrucciones: instrucciones instruccion
                    | instuccion
    '''                 

def p_instruccion(t):
    '''instruccion  : expl 

    '''

def p_expl(t):
    '''expl         : expl OR expm
                    | expl AND expm
                    | NOT expm
                    | expl EQUALS expm
                    | expl DIFERENTE expm
                    | expl MENOR expm
                    | expl MAYOR expm
                    | expl MAYORIGUAL expm
                    | expl MENORIGUAL expm
                    | expm
    '''
def p_expm(t):
    '''expm         : expm MAS expval
                    | expm MENOS expval
                    | expm POR expval
                    | expm DIVIDIDO expval
                    | expm MODULO expval
                    | expm ELEVADO expval
                    | expval
    '''

def p_expval(t):
    '''expval       : MENOS expl
                    | PAREA expl PAREC
                    | num
                    | CADENA
                    | CARACTER
                    | booleano
                    | ID
                    | nativa
    '''


def p_nativa(t):
    '''nativa       : LOG10 args
                    | LOG args
                    | SQRT args
    '''

def p_list_values(t):
    '''list_values  : list_values COMA expl
                    | expl
    '''

def p_args(t):
    'args           : PAREA list_values PAREC'

def p_booleano(t):
    '''booleano     : TRUE
                    | FALSE
    '''

def p_num(t):
    '''num          : ENTERO
                    | DECIMAL
    '''

def p_end_block(t):
    'end_block      : END sync'

def p_sync(t):
    'sync           : PTCOMA'

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)