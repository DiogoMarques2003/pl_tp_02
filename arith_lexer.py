import ply.lex as plex


class ArithLexer:
    tokens = (
        "NUM",  # numero inteiro
        "STRING",  # string delimitada por aspas duplas
        "FIM",  # atribuicao para o "FIM" das funções
        "FUNCAO",  # identificador de uma função
        "ESCREVER",  # identificador
        "VAR_ID",  # identificador de variável ou função
        "COMENTARIO",  # identificador de um comentario
        "SE",  # identificador de uma confição if
        "FIMSE",  # identificador de finalização da condição do SE
        "SENAO",  # identificador de uma condição else
        "NEG",  # Negação da condição do if
        "ENTRADA",  # Identificador para input de dados
        "MAP",  # Identificador para a função MAP
        "FOLD",  # Identificador para a função FOLD
        "CONCAT",  #Identificador de concatnação
    )

    literals = [
        '+',  # sinal de soma
        '-',  # sinal de subtração
        '*',  # sinal de multiplicação
        '/',  # sinal de divisão
        '=',  # sinal de igual
        '(',  # parêntese esquerdo
        ')',  # parêntese direito
        '[',  # parêntese reto esquerdo
        ']',  # parêntese reto direito
        '>',  # sinal de maior que
        '<',  # sinal de menor que
        ',',  # vírgula
        ';',  # ponto-e-vírgula
        ':',  # dois pontos
    ]

    # Ignorar espacos
    t_ignore = " \n"

    # Inicializa o lexer como None
    def __init__(self):
        self.lexer = None

    # Reconhecer numeros inteiros e decimais
    def t_NUM(self, t):
        r"[0-9]+(\.[0-9]+)?"
        if '.' in t.value:
            t.value = float(t.value)  # Se o número tiver "." converte para floar
        else:
            t.value = int(t.value)  # senão converte para int

        return t

    # Reconhecer a Palavra ESC ou ESCREVER
    def t_ESCREVER(self, t):
        # \b -> limite de palavra, garante que é exatamente o que está no regex
        r"[Ee][Ss][Cc]([Rr][Ee][Vv][Ee][Rr])?\b"
        return t

    # Reconhecer uma variavel e função
    def t_VAR_ID(self, t):
        # Deve iniciar por letra minuscula ou _
        # Depois pode ter qualquer letra minuscula/maiuscula e números
        # Pode terminar com ? ou !
        r"[a-z_][a-zA-Z0-9_]*[?!]?"
        return t

    # Reconhecedor de FIM
    def t_FIM(self, t):
        r"[Ff][Ii][Mm]"
        return t

    # Reconhecedor de FIMSE
    def t_FIMSE(self, t):
        r"[Ff][Ii][Mm][Ss][Ee]"
        return t

    # Reconhecedor de FUNCAO
    def t_FUNCAO(self, t):
        r"[Ff][Uu][Nn][Cc][Aa][Oo]"
        return t

    # Reconhecedor de uma string
    def t_STRING(self, t):
        # Proteção para não parar nos \"
        r'"(\\.|[^"\\])*"'
        t.value = t.value[1:-1]  # Remove aspas
        return t

    #Reconhecedor de COMENTARIO
    def t_COMENTARIO(self, t):
        # Reconhece comentários de uma linha iniciados por '--'
        # Reconhece comentários multilinha delimitados por '{--' e '--}', foi adicionado o [\s\S] para incluir quebras de linha
        r"(--[^\n]*|{-[\s\S]*?-})"
        return t

    #Reconhecedor de SE
    def t_SE(self, t):
        r"[Ss][Ee]"
        return t

    #Reconhecedor de SENAO
    def t_SENAO(self, t):
        r"[Ss][Ee][Nn][Aa][Oo]"
        return t

    #Reconhecedor de NEG (negação da condição)
    def t_NEG(self, t):
        r"[Nn][Ee][Gg]"
        return t

    #Reconhecedor de ENTRADA
    def t_ENTRADA(self, t):
        # \b -> limite de palavra, garante que é exatamente o que está no regex
        r"[Ee][Nn][Tt]([Rr][Aa][Dd][Aa])?\b"
        return t

    #Reconhecedor de MAP
    def t_MAP(self, t):
        r"[Mm][Aa][Pp]"
        return t

    #Reconhecedor de FOLD
    def t_FOLD(self, t):
        r"[Ff][Oo][Ll][Dd]"
        return t

    #Reconhecedor de CONCAT
    def t_CONCAT(self, t):
        r'<>'
        return t

    # cria o lexer
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    # define a entrada do lexer
    def input(self, string):
        self.lexer.input(string)

    # Obter proximo token do lexer
    def token(self):
        token = self.lexer.token()  # percorrer todos os tokens
        return token if token is None else token.type

    # Ocorre quando ocorre erro lexico
    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
