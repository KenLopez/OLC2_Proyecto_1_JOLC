from enum import Enum

class TYPE(Enum):
    TYPESTRING = 1
    TYPEINT64 = 2
    TYPEFLOAT64 = 3
    TYPEBOOL = 4
    TYPECHAR = 5
    FUNCTION = 6
    DOUBLE = 7
    NOTHING = 8
    ANY = 9
    STRUCT = 10
    LENGTH = 11
    IF = 12
    WHILE = 13
    FOR = 14
    LOGIC = 15
    ARITHMETIC = 16
    COMPARATIVE = 17
    GREATER = 18
    LOWER = 19
    GREATEREQUAL = 20
    LOWEREQUAL = 21
    EQUAL = 22
    DIFFERENT = 23
    NOT = 24
    ADDITION = 25
    SUBSTRACTION = 26
    DECLARATION = 27
    NATIVE = 28
    ASSIGN = 29
    FPRINT = 30
    FPRINTLN = 31
    MULTIPLICATION = 32
    DIVISION = 33
    POWER = 34
    MODULUS = 35
    NEGATE = 36
    FFLOAT = 37
    TYPEOF = 38
    SYMBOL = 39
    VARIBLE = 40
    STRUCTDEF = 41
    INMUTABLE = 42
    ERROR = 43
    PARAMETER = 44
    CALL = 45
    FSTRING = 46
    VALUETYPE = 47
    TRUNCATE = 48
    ROUND = 49
    TYPELIST = 50
    LOGICAND = 51
    LOGICOR = 52
    UPPERCASE = 53
    LOWERCASE = 54
    LOG10 = 55
    LOG = 56
    SQRT = 57
    COS = 58
    SIN = 59
    TAN = 60
    PARSE = 61
    LOCAL = 62
    GLOBAL = 63
    RANGE = 64
    PUSH = 65
    POP = 66
    CONTINUE = 67
    RETURN = 68
    BREAK = 69


names = {
    'TYPE.TYPESTRING': 'String',
    'TYPE.TYPEFLOAT64': 'Float64',
    'TYPE.TYPEINT64': 'Int64',
    'TYPE.TYPELIST': 'Array',
    'TYPE.TYPEBOOL': 'Boolean',
    'TYPE.NOTHING': 'Nothing',
    'TYPE.TYPECHAR': 'Char',
    'TYPE.TYPELIST': 'Array',
}
