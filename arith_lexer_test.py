# arith_lexer_test.py
from arith_lexer import ArithLexer

al = ArithLexer()
al.build()
al.input("(3-6)+9")  # "2++3") #"(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("num+2")  # "2++3") #"(3+5)*7")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input(""" x = 10  ; 
   y = 10 + 20 * 30;
   z = x * 100 ; 
   b =  a + 1 ; """)

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            ESC(_cart+_cart)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            FUNCAO soma (a, b)
                a + b
            FIM
            _Soma = soma(_cart?, _cart!)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""_cart? = 10, _cart! = 20;
            FUNCAO soma (a, b) :, a + b;
            _Soma = soma(_cart?, _cart!)""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")

print("\n-------\n")
al.input("""ESC("Teste")""")

while True:
    tk = al.token()
    if not tk:
        break
    print(tk, end="")
