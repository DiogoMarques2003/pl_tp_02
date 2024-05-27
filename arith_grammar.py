import re

from arith_lexer import ArithLexer
import ply.yacc as pyacc


class ArithGrammar:
    # Define a precedência dos operadores para resolver questões na gramatica
    precedence = (
        ('left', '+', '-'),  # Operadores de adição e subtração com associatividade à esquerda
        ('left', '*', '/'),  # Operadores de multiplicação e divisão com associatividade à esquerda
        ('right', 'UMINUS', 'UNARY_NEG'),  # Operadores unários como '-' (negativo) e 'NEG' têm associatividade à direita
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
            p[0] = {'op': 'seq', 'args': [p[1]]}  # uma única declaração
        else:
            p[1]['args'].append(p[2])  # Adiciona a declaração à lista existente
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
        """declaracao_atribuicao : VAR_ID '=' lista_expressoes ';'"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    # Multi declaração com/sem atribuição
    def p_declaracao_atribuicao_multipla(self, p):
        """declaracao_atribuicao : atribuicao
                                 | declaracao_atribuicao ',' atribuicao ';'"""
        if len(p) == 2:
            # Inicializa com uma única atribuição
            p[0] = {'op': 'seq', 'args': [p[1]]}
        else:
            # Mais de uma atribuição, agrupe-as em uma sequência
            if p[1].get('op') == 'seq':
                p[1]['args'].append(p[3])  # Adiciona a nova atribuição à sequência existente
            else:
                p[0] = {'op': 'seq', 'args': [p[1], p[3]]}  # Cria uma nova sequência
            p[0] = p[1]

    # atribuir o valor a var
    def p_atribuicao(self, p):
        """atribuicao : VAR_ID '=' expressao"""
        p[0] = {'op': 'atribuicao', 'args': [p[1], p[3]]}

    def p_lista_variaveis(self, p):
        """lista_variaveis : lista_variaveis ',' VAR_ID
                           | VAR_ID"""
        if len(p) == 2:
            p[0] = {'op': 'seq', 'args': [p[1]]}  # Inicia uma nova lista com o primeiro parâmetro
        else:
            p[1]['args'].append(p[3])  # Adiciona à lista existente
            p[0] = p[1]

    def p_lista_expressoes(self, p):
        """lista_expressoes : lista_expressoes ',' expressao
                            | expressao"""
        if len(p) == 2:
            p[0] = p[1]  # para uma única expressão, não envolva com 'seq'
        else:
            if not isinstance(p[1], list):
                p[1] = [p[1]]  # Se o primeiro item ainda não é uma lista, converta
            p[1].append(p[3])  # Adicione a expressão subsequente à lista
            p[0] = p[1]  # A lista é retornada diretamente

    # Declarações que são apenas expressões
    def p_declaracao_expressao(self, p):
        """declaracao_expressao : expressao ';'"""
        p[0] = p[1]

    # Expressões matemáticas básicas e literais
    def p_expressao(self, p):
        """expressao : expressao '+' expressao
                     | expressao '-' expressao
                     | expressao '*' expressao
                     | expressao '/' expressao
                     | expressao '=' '=' expressao
                     | expressao '<' expressao
                     | expressao '>' expressao
                     | expressao '<' '=' expressao
                     | expressao '>' '=' expressao
                     | expressao '!' '=' expressao"""

        if len(p) == 4:
            p[0] = {'op': p[2], 'args': [p[1], p[3]]}  # Cria objeto para a operação
        else:
            p[0] = {'op': ''.join([p[2], p[3]]), 'args': [p[1], p[4]]} # Para expressões onde tenhem mais que um operador

    # Expressões entre parênteses
    def p_expressao_grupo(self, p):
        """expressao : '(' expressao ')'"""
        p[0] = p[2]  # A expressão é diretamente o valor entre parênteses

    # Operador unário menos
    def p_expressao_uminus(self, p):
        """expressao : '-' expressao %prec UMINUS"""
        p[0] = {'op': 'uminus', 'args': [p[2]]}

    # Números
    def p_expressao_num(self, p):
        """expressao : NUM"""
        p[0] = {'op': 'literal', 'args': [p[1]]}

    # Strings
    def p_expressao_string(self, p):
        """expressao : STRING"""
        # Processar a string para obter partes interpoladas caso exista
        parts = self.process_interpolated_string(p[1])
        if len(parts) == 1:
            # se ouver apenas uma parte é porque é literal ou var
            if parts[0]['type'] == 'literal':
                p[0] = {'op': 'literal', 'args': [parts[0]['value']]}
            else:
                p[0] = {'var': parts[0]['value']}
        else:
            # construir a concatnação para a string com vares
            p[0] = {'op': 'concat', 'args': []}
            for part in parts:
                if part['type'] == 'literal':
                    p[0]['args'].append({'op': 'literal', 'args': [part['value']]})
                elif part['type'] == 'interpolacao':
                    # Adicionar a variável como uma expressão separada
                    p[0]['args'].append({'var': part['value']})

    # Variável
    def p_expressao_var_id(self, p):
        """expressao : VAR_ID"""
        p[0] = {'var': p[1]}

    # Array
    def p_expressao_var_array(self, p):
        """expressao : VAR_ID '[' ']'"""
        p[0] = {'array': p[1]}

    # Elementos array
    def p_expressao_array(self, p):
        """expressao : '[' lista_elementos  ']' """
        p[0] = {'elementos_array': p[2]}

    # array init
    def p_expressao_array_init(self, p):
        """declaracao_atribuicao : VAR_ID '[' ']' '=' '[' lista_elementos ']' ';'"""
        p[0] = {'op': 'array_init', 'args': [p[1], p[6]]}

    # Regra para lidar com a lista de elementos dentro dos colchetes
    def p_lista_elementos(self, p):
        """lista_elementos : lista_elementos ',' expressao
                           | expressao
                           | vazio"""
        if len(p) == 2:
            if p[1] is None:
                p[0] = []  # Lista vazia
            else:
                p[0] = [p[1]]  # Lista com um único elemento
        else:
            p[1].append(p[3])
            p[0] = p[1]  # Lista com múltiplos elementos

    # Função map
    def p_expressao_map(self, p):
        """expressao : MAP '(' VAR_ID ',' lista_expressoes ')'"""
        p[0] = {'op': 'map', 'args': [p[3], p[5]]}

    # Função fold
    def p_expressao_fold(self, p):
        """expressao : FOLD '(' VAR_ID ',' lista_expressoes ',' expressao ')'"""
        p[0] = {'op': 'fold', 'args': [p[3], p[5], p[7]]}

    # Função de entrada de valores
    def p_expressao_entrada(self, p):
        """expressao : ENTRADA '(' ')'"""
        p[0] = {'op': 'entrada'}

    # Função para gerar um número aleatorio
    def p_expressao_aleatorio(self, p):
        """expressao : ALEATORIO '(' NUM ')'"""
        p[0] = {'op': 'aleatorio', 'args': [p[3]]}

    #Chamar funções
    def p_expressao_chamada_funcao(self, p):
        """expressao : VAR_ID '(' lista_expressoes ')'"""
        if p[1] in ['map', 'fold']:  # se for a função map e fold a operação são eles mesmos
            p[0] = {'op': p[1], 'args': p[3]}
        else:
            p[0] = {'op': 'call_func', 'args': [p[1], p[3]]}

    # Declaração de funções
    def p_declaracao_funcao(self, p):
        """declaracao_funcao : FUNCAO VAR_ID '(' lista_parametros_opcional ')' ':'   FIM
                             | FUNCAO VAR_ID '(' lista_parametros_opcional ')' ',' ':' expressao ';'"""
        if len(p) == 10:
            # Esta é a forma da função: FUNCAO nome (parametros) ,: expressao;
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
                            | lista_parametros ',' NUM
                            | lista_parametros ',' array_vazio
                            | lista_parametros ',' var_array
                            | VAR_ID
                            | NUM
                            | array_vazio
                            | var_array"""
        if len(p) == 2:
            p[0] = [p[1]]  # Inicia uma nova lista com o primeiro parâmetro
        else:
            p[1].append(p[3])  # Adiciona à lista existente
            p[0] = p[1]

    # Array vazio
    def p_empty_list(self, p):
        """array_vazio : '[' ']'"""
        p[0] = []

    # VAR_ID:ARRAY
    def p_var_array(self, p):
        """var_array : VAR_ID ':' VAR_ID '[' ']' """

        p[0] = {'op': 'var_array', 'args': [p[1], p[3]]}

    # Declaração condicional 'se' com opcional 'senão'
    def p_declaracao_se(self, p):
        """declaracao_se : SE expressao ':' lista_declaracoes senao FIM"""
        p[0] = {'op': 'se', 'args': [p[2], p[4], p[5]]}

    # Parte opcional 'senao' e 'senaose' para a declaração condicional
    def p_senao_opcional(self, p):
        """senao : SENAO ':' lista_declaracoes
                 | SENAOSE expressao ':' lista_declaracoes
                 | vazio"""

        if len(p) == 4:
            p[0] = {'op': 'senao', 'args': p[3]}
        elif len(p) == 5:
            p[0] = {'op': 'senao_se', 'args': [p[2], p[4]]}
        else:
            p[0] = {'op': 'senao', 'args': []}

    # Negação da espreção das condições 'se' e 'senaose'
    def p_expressao_negacao(self, p):
        """expressao : NEG expressao %prec UNARY_NEG"""
        p[0] = {'op': 'neg', 'args': [p[2]]}

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
        """bloco_funcao : lista_declaracoes"""
        p[0] = p[1]

    # Tratar os erros que pode dar a resolver a gramatica do código
    def p_error(self, p):
        if p:
            print(f"Syntax error at token '{p.type}' with value '{p.value}' at line '{p.lineno}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)

    # Função para reconhecer interpolação das strings com variaveis
    def process_interpolated_string(self, text):
        parts = []
        # separar o texto pelas interpolações
        tokens = re.split(r'(\#\{[^}]+\})', text)
        for token in tokens:
            if token.startswith('#{') and token.endswith('}'):
                # remover o "#{" e "}" da interpolação
                expression = token[2:-1]
                parts.append({'type': 'interpolacao', 'value': expression})
            else:
                # é uma string
                parts.append({'type': 'literal', 'value': token})
        return parts