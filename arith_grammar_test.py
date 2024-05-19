# arith.py
from arith_grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

teste = ArithGrammar()
teste.build()

exemplos = [ # exemplos a avaliar de forma independente...
            'ESCREVER("ola mundo!");',
            'ESCREVER("PL " <> 2 <> "o ano de" <> "ESI");',
            'ESCREVER("soma de " <> 9 <> "com " <> 3*4 <> "=" <> 9+2*3);',
            'FUNCAO teste(a, b) ,: a+b;',
            'FUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM',
            'nome="diogo", idade=10;',
            "FUNCAO soma(a,b) ,: a+b ;\nFUNCAO soma2(c) :\nc = c+1 ;\nc+1 ;\nFIM\nseis = soma(4,2);\noito = soma2(seis);"
            ]
for frase in exemplos:
    print(f"----------------------")
    print(f"--- frase '{frase}'")
    resposta = teste.parse( frase )
    print("resultado: ")
    pp.pprint(resposta)