reservadas = {
    'end'       :   'END',
    'nothing'   :   'NOTHING',
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
    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENA',
    'CARACTER',
    'COMA',
    'DOSPT',
    'PT',
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
t_PT            = r'\.'

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
    r'[a-zA-Z_][a-zA-Z_0-9]*'
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

t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter no reconocido '%s'" % t.value[0])

from classes.Global import Global
from classes.Nodo import Nodo
from classes.Struct import Struct
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
from classes.StructAccess import StructAccess
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
    ('nonassoc', 'PT')
)

def p_init(t):
    'init           : globales'
    t[0] = Global()
    t[0].instrucciones = t[1][0]
    t[0].ast = t[1][1]

def p_globales_mult_1(t):
    'globales       : globales instruccion'
    t[1][0].append(t[2][0])
    t[0] = [t[1][0], Nodo('globales', [t[1][1], t[2][1]])]

def p_globales_mult_2(t):
    '''globales     : globales funcion END sync
                    | globales struct END sync
    '''
    t[1][0].append(t[2][0])
    t[0] = [t[1][0], Nodo('globales', [t[1][1], t[2][1], Nodo(t[3]), t[4]])]

def p_globales_1(t):
    '''globales     : funcion END sync
                    | struct END sync
    '''
    t[0] = [[t[1][0]], Nodo('globales', [t[1][1], Nodo(t[2]), t[3]])]

def p_globales_3(t):
    'globales       : instruccion'
    t[0] = [[t[1][0]], Nodo('globales', [t[1][1]])]

def p_struct(t):
    'struct         : STRUCT ID attributes'
    t[0] = [
        Declaracion(t[2], Struct(t[3][0], False, TYPE.STRUCTDEF), t.lexer.lineno, t.lexer.lexpos),
        Nodo('struct', [Nodo(t[1]), Nodo(t[2]), t[3][1]])
    ]

def p_struct_mutable(t):
    'struct         : MUTABLE STRUCT ID attributes'
    t[0] = [
        Declaracion(t[3], Struct(t[4][0], True, TYPE.STRUCTDEF), t.lexer.lineno, t.lexer.lexpos),
        Nodo('struct', [Nodo(t[1]), Nodo(t[2]), Nodo(t[3]), t[4][1]])
    ]

def p_attributes(t):
    'attributes     : attributes attribute'
    t[1][0].append(t[2][0])
    t[0] = [t[1][0], Nodo('attributes', [t[1][1], t[2][1]])]

def p_attributes_attribute(t):
    'attributes     : attribute'
    t[0] = [[t[1][0]], Nodo('attributes', [t[1][1]])]

def p_attribute(t):
    'attribute      : ID sync'
    t[0] = [Param(t[1], TYPE.ANY), Nodo('attribute', [Nodo(t[1]), t[2]])]

def p_attribute_type(t):
    'attribute      : ID DDOSPT typing sync'
    t[0] = [Param(t[1], t[3][0]), Nodo('attribute', [Nodo(t[1]), Nodo(t[2]), t[3][1], t[4]])]

def p_instrucciones_lista(t):
    'instrucciones  : instrucciones instruccion'
    t[1][0].append(t[2][0])
    t[0] = [t[1][0], Nodo('instrucciones', [t[1][1], t[2][1]])]

def p_instrucciones_instruccion(t):
    'instrucciones  :   instruccion'
    t[0] = [[t[1][0]], Nodo('instrucciones', [t[1][1]])]

def p_instruccion_while(t):
    'instruccion    : WHILE expl instrucciones END sync'
    t[0] = [
        While(t[2][0], t[3][0], t.lexer.lineno, t.lexer.lexpos),
        Nodo('instruccion', [Nodo(t[1]), t[2][1], t[3][1], Nodo(t[4]), t[5]])
    ]

def p_instruccion_for(t):
    'instruccion    : FOR ID IN range instrucciones END sync'
    t[0] = [
        For(t[2], t[4][0], t[5][0], t.lexer.lineno, t.lexer.lexpos), 
        Nodo('instruccion', [Nodo(t[1]), Nodo(t[2]), Nodo(t[3]), t[4][1], t[5][1], Nodo(t[6]), t[7]])
    ]

def p_range_expl(t):
    'range          : expval'
    t[0] = [t[1][0], Nodo('range', t[1][1])]

def p_range_range(t):
    'range          : expm DOSPT expm'
    t[0] = [Value([t[1][0], t[3][0]], TYPE.RANGE, t.lexer.lineno, t.lexer.lexpos), Nodo('range', [t[1][1], Nodo(t[2]), t[3][0]])]

def p_instruccion(t):
    '''instruccion  : PRINT args sync 
                    | PRINTLN args sync
    '''
    t[0] = [None, Nodo('instruccion', [Nodo(t[1]), t[2][1], t[3]])]
    if t[1] == 'print': t[0][0] = Print(t[2][0], TYPE.FPRINT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'println' : t[0][0] = Print(t[2][0], TYPE.FPRINTLN, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_asignacion(t):
    'instruccion    : asignacion sync'
    t[0] = [t[1][0], Nodo('instruccion', [t[1][1], t[2]])]

def p_instruccion_if(t):
    'instruccion    : if END sync'
    t[0] = [t[1][0], Nodo('instruccion', [t[1][1], Nodo(t[2]), t[3]])]

def p_instruccion_push(t):
    'instruccion    : PUSH NOT args sync'
    t[0] = [Nativa(t[3][0], TYPE.PUSH, t.lexer.lineno, t.lexer.lexpos), Nodo('instruccion', [Nodo(t[1]), Nodo(t[2]), t[3][1], t[4]])]

def p_instruccion_control(t):
    '''instruccion  : BREAK sync
                    | CONTINUE sync
                    | RETURN sync
    '''
    t[0] = [None, Nodo('instruccion', [t[1], t[2]])]
    if t[1] == 'break': t[0][0] = Control(None, TYPE.BREAK, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'continue': t[0][0] = Control(None, TYPE.CONTINUE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'return': t[0][0] = Control(None, TYPE.RETURN, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion_return_value(t):
    'instruccion    : RETURN expl sync'
    t[0] = [Control(t[2][0], TYPE.RETURN, t.lexer.lineno, t.lexer.lexpos), Nodo('instruccion', [Nodo(t[1]), t[2][1], t[3]])]

def p_instruccion_call(t):
    'instruccion    : call sync'
    t[0] = [t[1][0], Nodo('instruccion', [t[1][1], t[2]])]

def p_if_solo(t):
    'if             : IF expl instrucciones'
    t[0] = [
        If([t[2][0]], [t[3][0]], [], t.lexer.lineno, t.lexer.lexpos),
        Nodo('if', [Nodo(t[1]), t[2][1], t[3][1]])
    ]

def p_if_else(t):
    'if             : IF expl instrucciones ELSE instrucciones'
    t[0] = [
        If([t[2][0]], [t[3][0]], t[5][0], t.lexer.lineno, t.lexer.lexpos),
        Nodo('if', [Nodo(t[1]), t[2][1], t[3][1], Nodo(t[4]), t[5][1]])
    ]

def p_if_elseif(t):
    'if             : IF expl instrucciones elseif'
    con = [t[2][0]]
    con.extend(t[4][0][0])
    ins = [t[3][0]]
    ins.extend(t[4][0][1])
    t[0] = [
        If(con, ins, [], t.lexer.lineno, t.lexer.lexpos),
        Nodo('if', [Nodo(t[1]), t[2][1], t[3][1], t[4][1]])
    ]

def p_if_full(t):
    'if             : IF expl instrucciones elseif ELSE instrucciones'
    con = [t[2][0]]
    con.extend(t[4][0][0])
    ins = [t[3][0]]
    ins.extend(t[4][0][1])
    t[0] = [
        If(con, ins, t[6][0], t.lexer.lineno, t.lexer.lexpos),
        Nodo('if', [Nodo(t[1]), t[2][1], t[3][1], t[4][1], Nodo(t[5]), t[6][1]])
    ]

def p_if_elseifs(t):
    'elseif         : elseif ELSEIF expl instrucciones'
    t[1][0][0].append(t[3][0])
    t[1][0][1].append(t[4][0])
    t[0] = [t[1][0], Nodo('elseif', [t[1][1], Nodo(t[2]), t[3][1], t[4][1]])]

def p_elseif(t):
    'elseif         : ELSEIF expl instrucciones'
    t[0] = [[[t[2][0]], [t[3][0]]], Nodo('elseif', [Nodo(t[1]), t[2][1], t[3][1]])]

def p_asignacion_any(t):
    'asignacion     : variable IGUAL expl'
    t[0] = [ 
        Asignacion(t[1][0][0], t[3][0], TYPE.ANY, t[1][0][1], t.lexer.lineno, t.lexer.lexpos),
        Nodo('asignacion', [t[1][1], Nodo(t[2]), t[3][1]])
    ]

def p_asignacion_tipo(t):
    'asignacion     : variable IGUAL expl DDOSPT typing'
    t[0] = [
        Asignacion(t[1][0][0], t[3][0], t[5][0], t[1][0][1], t.lexer.lineno, t.lexer.lexpos),
        Nodo('asignacion', [t[1][1], Nodo(t[2]), t[3][1], Nodo(t[4]), t[5][1]])
    ]

def p_declaracion_none(t):
    'asignacion     : variable'
    t[0] = [
        Asignacion(t[1][0][0], None, TYPE.ANY, t[1][0][1], t.lexer.lineno, t.lexer.lexpos),
        Nodo('asignacion', [t[1][1]])
    ]

def p_funcion(t):
    'funcion        : FUNCTION ID params instrucciones'
    t[0] = [
        Declaracion(t[2], Funcion(t[3][0], t[4][0]), t.lexer.lineno, t.lexer.lexpos),
        Nodo('funcion', [Nodo(t[1]), Nodo(t[2]), t[3][1], t[4][1]])
    ]

def p_params(t):
    'params         : PAREA list_params PAREC'
    t[0] = [t[2][0], Nodo('params', [Nodo(t[1]), t[2][1], Nodo(t[3])])]

def p_params_none(t):
    'params         : PAREA PAREC'
    t[0] = [[], Nodo('params', [Nodo(t[1]), Nodo(t[2])] )]

def p_call(t):
    'call           : ID args'
    t[0] = [Call(t[1], t[2][0], t.lexer.lineno, t.lexer.lexpos), Nodo('call', [Nodo(t[1]), t[2][1]])]

def p_list_params(t):
    'list_params    : list_params COMA param'
    t[1][0].append(t[3][0])
    t[0] = [t[1][0], Nodo('list_params', [t[1][1], Nodo(t[2]), t[3][1]])]

def p_list_param(t):
    'list_params    : param'
    t[0] = [[t[1][0]], Nodo('list_params', [t[1][1]])]

def p_param(t):
    'param          : ID'
    t[0] = [Param(t[1], TYPE.ANY), Nodo('param', [Nodo(t[1])])]

def p_param_type(t):
    'param          : ID DDOSPT typing'
    t[0] = [Param(t[1], t[3][0]), Nodo('param', [Nodo(t[1]), Nodo(t[2]), t[3][1]])]

def p_variable_id(t):
    'variable       : id'
    t[0] = [[t[1][0], TYPE.NOTHING], Nodo('variable', [t[1][1]])]

def p_variable_struct(t):
    'variable       : ID PT struct_access'
    t[0] = [
        [StructAccess(Variable(t[1], t.lexer.lineno, t.lexer.lexpos), t[3][0], t.lexer.lineno, t.lexer.lexpos), TYPE.NOTHING],
        Nodo('variable', [Nodo(t[1]), Nodo(t[2]), t[3][1]])
    ]

def p_variable_local(t):
    'variable       : LOCAL ID'
    t[0] = [[t[2], TYPE.LOCAL], Nodo('variable', [Nodo(t[1]), Nodo(t[2])])]

def p_variable_global(t):
    'variable       : GLOBAL ID'
    t[0] = [[t[2], TYPE.GLOBAL], Nodo('variable', [Nodo(t[1]), Nodo(t[2])])]

def p_id_id(t):
    'id         : ID'
    t[0] = [t[1], Nodo('id', [Nodo(t[1])])]

def p_id_array_access(t):
    'id         : ID array_access'
    t[0] = [
        ArrayAccess(Variable(t[1], t.lexer.lineno, t.lexer.lexpos), t[2][0], t.lexer.lineno, t.lexer.lexpos), 
        Nodo('id', [t[1][1], t[2][1]])
    ]

def p_expl(t):
    '''expl         : expl OR expl
                    | expl AND expl
    '''
    t[0] = [None, Nodo('expr', [t[1][1], Nodo(t[2]), t[3][1]])]
    if t[2] == '||': t[0][0] = Logica(t[1][0], t[3][0], TYPE.LOGICOR, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '&&': t[0][0] = Logica(t[1][0], t[3][0], TYPE.LOGICAND, t.lexer.lineno, t.lexer.lexpos)

def p_expl_expr(t):
    'expl           : expr'
    t[0] = [t[1][0], Nodo('expl', [t[1][1]])]

def p_expr(t):
    '''expr         : expr EQUALS expr
                    | expr DIFERENTE expr
                    | expr MENOR expr
                    | expr MAYOR expr
                    | expr MAYORIGUAL expr
                    | expr MENORIGUAL expr
    
    '''
    t[0] = [None, Nodo('expr', [t[1][1], Nodo(t[2]), t[3][1]])]
    if t[2] == '==': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.EQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '!=': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.DIFFERENT, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '<=': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.LOWEREQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '>=': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.GREATEREQUAL, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '<': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.LOWER, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '>': t[0][0] = Relacional(t[1][0], t[3][0], TYPE.GREATER, t.lexer.lineno, t.lexer.lexpos)

def p_expr_expm(t):
    'expr           : expm'
    t[0] = [t[1][0], Nodo('expr', [t[1][1]])]

def p_expm(t):
    '''expm         : expm MAS expm
                    | expm MENOS expm
                    | expm POR expm
                    | expm DIVIDIDO expm
                    | expm MODULO expm
                    | expm ELEVADO expm
    '''
    t[0] = [None, Nodo('expm', [t[1][1], Nodo(t[2]), t[3][1]])]
    if t[2] == '+': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.ADDITION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '-': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.SUBSTRACTION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '*': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.MULTIPLICATION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '/': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.DIVISION, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '%': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.MODULUS, t.lexer.lineno, t.lexer.lexpos)
    elif t[2] == '^': t[0][0] = Aritmetica(t[1][0], t[3][0], TYPE.POWER, t.lexer.lineno, t.lexer.lexpos)


def p_expm_val(t):
    'expm           : expval'
    t[0] = [t[1][0], Nodo('expm', [t[1][1]])]

def p_expval_not(t):
    'expval         : NOT expval'
    t[0] = [
        Logica(t[2][0], None, TYPE.NOT, t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1], t[2][1])])
    ]

def p_expval_neg(t):
    'expval         : MENOS expval'
    t[0] = [
        Aritmetica(Value(-1, TYPE.TYPEINT64, t.lexer.lineno, t.lexer.lexpos), t[2][0], TYPE.MULTIPLICATION, t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1]), t[2][1]])
    ]

def p_expval_string(t):
    'expval         : CADENA'
    t[0] = [Value(t[1], TYPE.TYPESTRING, t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [Nodo(t[1])])]

def p_expval_char(t):
    'expval         : CARACTER'
    t[0] = [Value(t[1], TYPE.TYPECHAR, t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [Nodo(t[1])])]

def p_expval_bool(t):
    'expval         : booleano'
    t[0] = [Value(t[1][0], TYPE.TYPEBOOL, t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [t[1][1]])]

def p_expval_int(t):
    'expval         : ENTERO'
    t[0] = [Value(t[1], TYPE.TYPEINT64, t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [Nodo(str(t[1]))])]

def p_expval_float(t):
    'expval         : DECIMAL'
    t[0] = [Value(t[1], TYPE.TYPEFLOAT64, t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [Nodo(str(t[1]))])]

def p_expval_nativa(t):
    'expval         : nativa'
    t[0] = [t[1][0], Nodo('expval', [t[1][1]])]

def p_expval_id(t):
    'expval         : ID'
    t[0] = [Variable(t[1], t.lexer.lineno, t.lexer.lexpos), Nodo('expval', [Nodo(t[1])])]

def p_expval_call(t):
    'expval         : call'
    t[0] = [t[1][0], Nodo('expval',[t[1][1]])]

def p_expval_paren(t):
    'expval         : PAREA expl PAREC'
    t[0] = [t[2][0], Nodo('expval', [Nodo(t[1]), t[2][1], Nodo(t[3])])]

def p_expval_type(t):
    '''expval       : INT64
                    | FLOAT64
    '''
    t[0] = [None, Nodo('expval', [Nodo(t[1])])]
    if t[1] == 'Int64': t[0][0] = Value(TYPE.TYPEINT64, TYPE.VALUETYPE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'Float64': t[0][0] = Value(TYPE.TYPEFLOAT64, TYPE.VALUETYPE, t.lexer.lineno, t.lexer.lexpos)

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
    '''
    t[0] = [None, Nodo('nativa', [Nodo(t[1]), t[2][1]])]
    if t[1] == 'uppercase': t[0][0] = Nativa(t[2][0], TYPE.UPPERCASE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'lowercase': t[0][0] = Nativa(t[2][0], TYPE.LOWERCASE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'log10': t[0][0] = Nativa(t[2][0], TYPE.LOG10, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'log': t[0][0] = Nativa(t[2][0], TYPE.LOG, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'sin': t[0][0] = Nativa(t[2][0], TYPE.SIN, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'cos': t[0][0] = Nativa(t[2][0], TYPE.COS, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'tan': t[0][0] = Nativa(t[2][0], TYPE.TAN, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'sqrt': t[0][0] = Nativa(t[2][0], TYPE.SQRT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'parse': t[0][0] = Nativa(t[2][0], TYPE.PARSE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'trunc': t[0][0] = Nativa(t[2][0], TYPE.TRUNCATE, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'string': t[0][0] = Nativa(t[2][0], TYPE.FSTRING, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'float': t[0][0] = Nativa(t[2][0], TYPE.FFLOAT, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'typeof': t[0][0] = Nativa(t[2][0], TYPE.TYPEOF, t.lexer.lineno, t.lexer.lexpos)
    elif t[1] == 'length': t[0][0] = Nativa(t[2][0], TYPE.LENGTH, t.lexer.lineno, t.lexer.lexpos)

def p_nativa_pop(t):
    'nativa         : POP NOT args'
    t[0] = [Nativa(t[3][0], TYPE.POP, t.lexer.lineno, t.lexer.lexpos), Nodo('nativa', [Nodo(t[1]), Nodo(t[2]), t[3][1]])]

def p_expval_array(t):
    'expval         : CORCHEA list_values CORCHEC'
    t[0] = [
        Value(t[2][0], TYPE.TYPELIST, t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1]), t[2][0], Nodo(t[2])])
    ]

def p_expval_empty_array(t):
    'expval         : CORCHEA CORCHEC'
    t[0] = [
        Value([], TYPE.TYPELIST, t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1]), Nodo(t[2])])
    ]

def p_expval_array_access(t):
    'expval         : ID array_access'
    t[0] = [
        ArrayAccess(Variable(t[1], t.lexer.lineno, t.lexer.lexpos), t[2][0], t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1]), t[2][1]])
    ]

def p_expval_nothing(t):
    'expval         : NOTHING'
    t[0] = [
        Value(None, TYPE.NOTHING, t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1])])
    ]

def p_expval_struct_access(t):
    'expval         : ID PT struct_access'
    t[0] = [
        StructAccess(Variable(t[1], t.lexer.lineno, t.lexer.lexpos), t[3][0], t.lexer.lineno, t.lexer.lexpos),
        Nodo('expval', [Nodo(t[1]), Nodo(t[2]), t[3][1]])
    ]

def p_array_accesses(t):
    'array_access   : array_access CORCHEA expm CORCHEC'
    t[1][0].append(t[3][0])
    t[0] = [t[1][0], Nodo('array_access', [t[1][1], Nodo(t[2]), t[3][1], Nodo(t[4])])]

def p_array_access(t):
    'array_access   : CORCHEA expm CORCHEC'
    t[0] = [[t[2][0]], Nodo('array_access', [Nodo(t[1]), t[2][1], Nodo(t[3])])]

def p_struct_accesses(t):
    'struct_access   : struct_access PT ID'
    t[1][0].append(t[3])
    t[0] = [t[1][0], Nodo('struct_access', [t[1][1], Nodo(t[2]),Nodo(t[3])])]

def p_struct_access(t):
    'struct_access   : ID'
    t[0] = [[t[1]], Nodo('struct_access', [Nodo(t[1])])]

def p_list_values(t):
    'list_values    : list_values COMA expl'
    t[1][0].append(t[3][0])
    t[0] = [t[1][0], Nodo('list_values', [t[1][1]])]

def p_list_value(t):
    'list_values    : expl'
    t[0] = [[t[1][0]], Nodo('list_values', [t[1][1]])]

def p_args(t):
    'args           : PAREA list_values PAREC'
    t[0] = [t[2][0], Nodo('args', [Nodo(t[1]), t[2][1], Nodo(t[3])])]

def p_args_none(t):
    'args           : PAREA PAREC'
    t[0] = [[], Nodo('args', [Nodo(t[1]), Nodo(t[2])])]

def p_booleano(t):
    '''booleano     : TRUE
                    | FALSE
    '''
    if t[1] == 'true': t[0] = [True, Nodo('booleano', [Nodo(t[1])])]
    elif t[1] == 'false': t[0] = [False, Nodo('booleano', [Nodo(t[1])])]


def p_typing(t):
    '''typing       : INT64
                    | FLOAT64
                    | STRING
                    | BOOL
                    | CHAR
                    | ID
    '''
    if t[1]=='Int64': t[0] = [TYPE.TYPEINT64, Nodo('typing', [Nodo(t[1])])]
    elif t[1]=='Float64': t[0] = [TYPE.TYPEFLOAT64, Nodo('typing', [Nodo(t[1])])]
    elif t[1]=='String': t[0] = [TYPE.TYPESTRING, Nodo('typing', [Nodo(t[1])])]
    elif t[1]=='Bool': t[0] =[TYPE.TYPEBOOL, Nodo('typing', [Nodo(t[1])])]
    elif t[1]=='Char': t[0] = [TYPE.TYPECHAR, Nodo('typing', [Nodo(t[1])])]
    else: t[0] = [t[1], Nodo('typing', [Nodo(t[1])])]

def p_sync(t):
    'sync           : PTCOMA'
    t[0] = Nodo('sync', [Nodo(t[1])])

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)