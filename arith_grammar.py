# arith_grammar.py
from arith_lexer import ArithLexer
import ply.yacc as pyacc


class ArithGrammar:
    # Define a precedência dos operadores para resolver questões na gramatica
    precedence = (
        ('left', '+', '-'),  # Operadores de adição e subtração com associatividade à esquerda
        ('left', '*', '/'),  # Operadores de multiplicação e divisão com associatividade à esquerda
        ('right', 'UMINUS'),  # Menos unário com associatividade à direita
    )

    # Constructor
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    # Construir o analisador sintatico, pega no lexer e configura-o
    def build(self, **kwargs):
        self.lexer = ArithLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    # Realiza a analise sintatica do Input fornecido
    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # Regras Producao da Gramatica:

    # Lista de declarações, que pode ser uma única declaração ou várias declarações
    def p_lista_declaracoes(self, p):
        """lista_declaracoes : declaracao
                             | lista_declaracoes declaracao"""
        if len(p) == 2:
            p[0] = [p[1]]  # uma única declaração
        else:
            p[1].append(p[3])  # Adiciona a declaração à lista existente
            p[0] = p[1]

    # Declarações gerais dentro do programa
    def p_declaracao(self, p):
        """declaracao : declaracao_atribuicao
                      | declaracao_expressao
                      | declaracao_funcao
                      | declaracao_se
                      | declaracao_escrever
                      | declaracao_comentario"""
        p[0] = p[1]

    # Declaração com atribuição
    def p_declaracao_atribuicao(self, p):
        """declaracao_atribuicao : VAR_ID '=' expressao ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Declarações que são apenas expressões
    def p_declaracao_expressao(self, p):
        """declaracao_expressao : expressao ';'"""
        p[0] = p[1]

    # Expressões matemáticas básicas e literais
    def p_expressao(self, p):
        """expressao : expressao '+' expressao
                     | expressao '-' expressao
                     | expressao '*' expressao
                     | expressao '/' expressao"""
        p[0] = {'op': p[2], 'args': [p[1], p[3]]}  # Cria objeto para a operação

    # Expressões entre parênteses
    def p_expressao_grupo(self, p):
        """expressao : '(' expressao ')'"""
        p[0] = p[2]  # A expressão é diretamente o valor entre parênteses

    # Operador unário menos
    def p_expressao_uminus(self, p):
        """expressao : '-' expressao %prec UMINUS"""
        p[0] = {'op': 'uminus', 'args': [p[2]]}

    # Números, variáveis e strings como literais
    def p_expressao_num_id(self, p):
        """expressao : NUM
                     | VAR_ID
                     | STRING"""
        p[0] = {'op': 'literal', 'args': p[1]}

    # Declaração de funções
    def p_declaracao_funcao(self, p):
        """declaracao_funcao : FUNCAO VAR_ID '(' lista_parametros_opcional ')' ':' bloco_funcao FIM
                             | FUNCAO VAR_ID '(' lista_parametros_opcional ')' ',' ':' expressao ';'"""
        if len(p) == 10:
            # Esta é a forma concisa da função: FUNCAO nome (parametros) ,: expressao;
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[8]]}  # Captura a expressão em p[8]
        else:
            p[0] = {'op': 'funcao', 'args': [p[2], p[4], p[7]]}

    # Lista opcional de parâmetros para funções
    def p_lista_parametros_opcional(self, p):
        """lista_parametros_opcional : lista_parametros
                                     | vazio"""
        p[0] = p[1]

    # Lista de parâmetros para funções
    def p_lista_parametros(self, p):
        """lista_parametros : lista_parametros ',' VAR_ID
                            | VAR_ID"""
        if len(p) == 2:
            p[0] = [p[1]]  # Inicia uma nova lista com o primeiro parâmetro
        else:
            p[1].append(p[3])  # Adiciona à lista existente
            p[0] = p[1]

    # Declaração condicional 'se' com opcional 'senão'
    def p_declaracao_se(self, p):
        """declaracao_se : SE expressao ':' lista_declaracoes senao_opcional FIM"""
        p[0] = {'op': 'se', 'args': [p[2], p[4], p[5]]}

    # Parte opcional 'senão' para a declaração condicional
    def p_senao_opcional(self, p):
        """senao_opcional : SENAO ':' lista_declaracoes
                          | vazio"""
        p[0] = p[1]

    # Declaração para escrita (output)
    def p_declaracao_escrever(self, p):
        """declaracao_escrever : ESCREVER '(' expressao ')' ';'"""
        p[0] = {'op': 'escrever', 'args': p[3]}

    # Tratamento de comentários no código
    def p_declaracao_comentario(self, p):
        """declaracao_comentario : COMENTARIO"""
        p[0] = {'op': 'comentario', 'args': p[1]}

    # Produção vazia para elementos opcionais
    def p_vazio(self, p):
        """vazio :"""
        p[0] = None

    # Conctnação
    def p_expressao_concat(self, p):
        """expressao : expressao CONCAT expressao"""
        p[0] = {'op': 'concat', 'args': [p[1], p[3]]}

    # Bloco de funções que pode ser uma lista de declarações ou uma expressão simples
    def p_bloco_funcao(self, p):
        """bloco_funcao : lista_declaracoes
                        | expressao ';'"""
        if len(p) == 2:
            p[0] = [p[1]]  # Trata a expressão como uma declaração única
        else:
            p[0] = p[1]

    # Tratar os erros que pode dar a resolver a gramatica do código
    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)