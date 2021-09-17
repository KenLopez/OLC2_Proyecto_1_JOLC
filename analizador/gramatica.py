reservadas = {
    'end'       :   'END',
    'nothing'   :   'NOTHING',
    'Int64'     :   'INT64',
    'Float64'   :   'FLOAT64',
    'Bool'      :   'BOOL',
    'Char'      :   'CHAR',
    'String'    :   'STRING',
    #'struct'    :   'STRUCT',
    'log'       :   'LOG',
    'log10'     :   'LOG10',
    'sin'       :   'SIN',
    'cos'       :   'COS',
    'tan'       :   'TAN',
    'sqrt'      :   'SQRT',
    'print'     :   'PRINT',
    'println'   :   'PRINTLN',
    'local'     :   'LOCAL',
    'global'    :   'GLOBAL',
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
    'for'       :   'FOR',
    'in'        :   'IN',
    'break'     :   'BREAK',
    'continue'  :   'CONTINUE',
    'return'    :   'RETURN',
    #'mutable'   :   'MUTABLE',
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
    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENA',
    'CARACTER',
    'COMA',
    'DOSPT',
] + list(reservadas.values())

# Tokens
t_PTCOMA        = r';'
t_CORCHEA       = r'\['
t_CORCHEC       = r'\]'
t_DDOSPT        = r'::'
t_DOSPT         = r':'        
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

from classes.Declaracion import Declaracion
from classes.Call import Call
from classes.Funcion import Funcion
from classes.Param import Param
from classes.Control import Control
from classes.For import For
from classes.ArrayAccess import ArrayAccess
from classes.While import While
from classes.If import If
from classes.Variable import Variable
from classes.Asignacion import Asignacion
from classes.Nativa import Nativa
from classes.Tipo import TYPE
from classes.Value import Value
from classes.Aritmetica import Aritmetica
from classes.Print import Print
from classes.Logica import Logica
from classes.Relacional import Relacional
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
)

def p_init(t):
    'init           : globales'
    t[0] = t[1]

def p_globales(t):
    '''globales     : globales instruccion
                    | globales funcion END sync
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_globales_2(t):
    '''globales     : funcion END sync
                    | instruccion
    '''
    t[0] = [t[1]]

def p_instrucciones_lista(t):
    'instrucciones  : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones  :   instruccion'
    t[0] = [t[1]]

def p_instruccion_while(t):
    'instruccion    : WHILE expl instrucciones END sync'
    t[0] = While(t[2], t[3], t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_for(t):
    'instruccion    : FOR ID IN range instrucciones END sync'
    t[0] = For(t[2], t[4], t[5], t.lexer.lineno, t.lexer.lexpos)

def p_range_expl(t):
    'range          : expl'
    t[0] = t[1]

def p_range_range(t):
    'range          : expl DOSPT expl'
    t[0] = Value([t[1], t[3]], TYPE.RANGE, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion(t):
    '''instruccion  : PRINT args sync 
                    | PRINTLN args sync
    '''
    if t[1] == 'print': t[0] = Print(t[2], TYPE.FPRINT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'println' : t[0] = Print(t[2], TYPE.FPRINTLN, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_asignacion(t):
    'instruccion    : asignacion sync'
    t[0] = t[1]

def p_instruccion_if(t):
    'instruccion    : if END sync'
    t[0] = t[1]

def p_instruccion_push(t):
    'instruccion    : PUSH NOT args sync'
    t[0] = Nativa(t[3], TYPE.PUSH, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_control(t):
    '''instruccion  : BREAK sync
                    | CONTINUE sync
                    | RETURN sync
    '''
    if t[1] == 'break': t[0] = Control(None, TYPE.BREAK, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'continue': t[0] = Control(None, TYPE.CONTINUE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'return': t[0] = Control(None, TYPE.RETURN, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_return_value(t):
    'instruccion    : RETURN expl sync'
    t[0] = Control(t[2], TYPE.RETURN, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_call(t):
    'instruccion    : call sync'
    t[0] = t[1]

def p_if_solo(t):
    'if             : IF expl instrucciones'
    t[0] = If([t[2]], [t[3]], [], t.lexer.lineno, t.lexer.lexpos)

def p_if_else(t):
    'if             : IF expl instrucciones ELSE instrucciones'
    t[0] = If([t[2]], [t[3]], t[5], t.lexer.lineno, t.lexer.lexpos)

def p_if_elseif(t):
    'if             : IF expl instrucciones elseif'
    con = [t[2]]
    con.extend(t[4][0])
    ins = [t[3]]
    ins.extend(t[4][1])
    t[0] = If(con, ins, [], t.lexer.lineno, t.lexer.lexpos)

def p_if_full(t):
    'if             : IF expl instrucciones elseif ELSE instrucciones'
    con = [t[2]]
    con.extend(t[4][0])
    ins = [t[3]]
    ins.extend(t[4][1])
    t[0] = If(con, ins, t[6], t.lexer.lineno, t.lexer.lexpos)

def p_if_elseifs(t):
    'elseif         : elseif ELSEIF expl instrucciones'
    t[1][0].append(t[3])
    t[1][1].append(t[4])
    t[0] = t[1]

def p_elseif(t):
    'elseif         : ELSEIF expl instrucciones'
    t[0] = [[t[2]], [t[3]]]

def p_asignacion_any(t):
    'asignacion     : variable IGUAL expl'
    t[0] = Asignacion(t[1][0], t[3], TYPE.ANY, t[1][1], t.lexer.lineno, t.lexer.lexpos)

def p_asignacion_tipo(t):
    'asignacion     : variable IGUAL expl DDOSPT typing'
    t[0] = Asignacion(t[1][0], t[3], t[5], t[1][1], t.lexer.lineno, t.lexer.lexpos)

def p_declaracion_none(t):
    'asignacion     : variable'
    t[0] = Asignacion(t[1][0], None, TYPE.ANY, t[1][1], t.lexer.lineno, t.lexer.lexpos)

def p_funcion(t):
    'funcion        : FUNCTION ID params instrucciones'
    t[0] = Declaracion(t[2], Funcion(t[3], t[4]), t.lexer.lineno, t.lexer.lexpos)

def p_params(t):
    'params         : PAREA list_params PAREC'
    t[0] = t[2]

def p_params_none(t):
    'params         : PAREA PAREC'
    t[0] = []

def p_call(t):
    'call           : ID args'
    t[0] = Call(t[1], t[2], t.lexer.lineno, t.lexer.lexpos)

def p_list_params(t):
    'list_params    : list_params COMA param'
    t[1].append(t[3])
    t[0] = t[1]

def p_list_param(t):
    'list_params    : param'
    t[0] = [t[1]]

def p_param(t):
    'param          : ID'
    t[0] = Param(t[1], TYPE.ANY)

def p_param_type(t):
    'param          : ID DDOSPT typing'
    t[0] = Param(t[1], t[3])

def p_variable_id(t):
    'variable       : id'
    t[0] = [t[1], TYPE.NOTHING]

def p_variable_local(t):
    'variable       : LOCAL id'
    t[0] = [t[2], TYPE.LOCAL]

def p_variable_global(t):
    'variable       : GLOBAL id'
    t[0] = [t[2], TYPE.GLOBAL]

def p_id_id(t):
    'id         : ID'
    t[0] = t[1]

def p_id_array_access(t):
    'id         : expval array_access'
    t[0] = ArrayAccess(t[1], t[2], t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = Logica(t[2], None, TYPE.NOT, t.lexer.lineno, t.lexer.lexpos)

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
    t[0] = t[1]

def p_expval_id(t):
    'expval         : ID'
    t[0] = Variable(t[1], t.lexer.lineno, t.lexer.lexpos)

def p_expval_call(t):
    'expval         : call'
    t[0] = t[1]

def p_expval_nothing(t):
    'expval         : NOTHING'
    t[0] = Value(None, TYPE.NOTHING, t.lexer.lineno, t.lexer.lexpos)

def p_expval_paren(t):
    'expval         : PAREA expl PAREC'
    t[0] = t[2]

def p_expval_type(t):
    '''expval       : INT64
                    | FLOAT64
    '''
    if t[1] == 'Int64': t[0] = Value(TYPE.TYPEINT64, TYPE.VALUETYPE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'Float64': t[0] = Value(TYPE.TYPEFLOAT64, TYPE.VALUETYPE, t.lexer.lineno, t.lexer.lexpos)

def p_nativa(t):
    '''nativa       : LOG10 args
                    | LOG args
                    | SQRT args
                    | LOWERCASE args
                    | UPPERCASE args
                    | SIN args
                    | COS args
                    | TAN args
                    | PARSE args
                    | TRUNC args
                    | FLOAT args
                    | FSTRING args
                    | TYPEOF args
                    | LENGTH args
                    | PUSH NOT args
                    | POP NOT args
    '''
    if t[1] == 'uppercase': t[0] = Nativa(t[2], TYPE.UPPERCASE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'lowercase': t[0] = Nativa(t[2], TYPE.LOWERCASE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'log10': t[0] = Nativa(t[2], TYPE.LOG10, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'log': t[0] = Nativa(t[2], TYPE.LOG, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'sin': t[0] = Nativa(t[2], TYPE.SIN, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'cos': t[0] = Nativa(t[2], TYPE.COS, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'tan': t[0] = Nativa(t[2], TYPE.TAN, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'sqrt': t[0] = Nativa(t[2], TYPE.SQRT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'parse': t[0] = Nativa(t[2], TYPE.PARSE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'trunc': t[0] = Nativa(t[2], TYPE.TRUNCATE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'string': t[0] = Nativa(t[2], TYPE.FSTRING, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'float': t[0] = Nativa(t[2], TYPE.FFLOAT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'typeof': t[0] = Nativa(t[2], TYPE.TYPEOF, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'length': t[0] = Nativa(t[2], TYPE.LENGTH, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'pop': t[0] = Nativa(t[3], TYPE.POP, t.lexer.lineno, t.lexer.lexpos)


def p_expval_array(t):
    'expval         : CORCHEA list_values CORCHEC'
    t[0] = Value(t[2], TYPE.TYPELIST, t.lexer.lineno, t.lexer.lexpos)

def p_expval_empty_array(t):
    'expval         : CORCHEA CORCHEC'
    t[0] = Value([], TYPE.TYPELIST, t.lexer.lineno, t.lexer.lexpos)

def p_expval_array_access(t):
    'expval         : expval array_access'
    t[0] = ArrayAccess(t[1], t[2], t.lexer.lineno, t.lexer.lexpos)

def p_array_accesses(t):
    'array_access   : array_access CORCHEA expm CORCHEC'
    t[1].append(t[3])
    t[0] = t[1]

def p_array_access(t):
    'array_access   : CORCHEA expm CORCHEC'
    t[0] = [t[2]]

def p_list_values(t):
    'list_values    : list_values COMA expl'
    t[1].append(t[3])
    t[0] = t[1]

def p_list_value(t):
    'list_values    : expl'
    t[0] = [t[1]]

def p_args(t):
    'args           : PAREA list_values PAREC'
    t[0] = t[2]

def p_args_none(t):
    'args           : PAREA PAREC'
    t[0] = []

def p_booleano(t):
    '''booleano     : TRUE
                    | FALSE
    '''
    if t[1] == 'true': t[0] = True
    elif t[1] == 'false': t[0] = False


def p_typing(t):
    '''typing       : INT64
                    | FLOAT64
                    | STRING
                    | BOOL
                    | CHAR
    '''
    if t[1]=='Int64': t[0] = TYPE.TYPEINT64
    elif t[1]=='Float64': t[0] = TYPE.TYPEFLOAT64
    elif t[1]=='String': t[0] = TYPE.TYPESTRING
    elif t[1]=='Bool': t[0] = TYPE.TYPEBOOL
    elif t[1]=='Char': t[0] = TYPE.TYPECHAR

def p_sync(t):
    'sync           : PTCOMA'

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)