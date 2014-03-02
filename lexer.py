import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'PROP_VAR',
   'NEG',
   'ARROW',
   'OR',
   'AND',
   'IFF',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PROP_VAR    = r'[a-z]'
t_NEG   = r'NOT' #Propositional variables are lower case and connectives are upper case to avoid prop_vars being found inside connectives.
t_ARROW   = r'ARROW'
t_OR  = r'OR'
t_AND = r'AND'
t_IFF = r'IFF'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

precedence = (
        ('right', 'NOT'),
        ('left', 'ARROW', 'OR', 'AND', 'IFF'),
        )

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    #test it out
    data = '((p OR q) ARROW         r) '

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok

