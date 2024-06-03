# arith_eval
import random


class ArithEval:
    # guardar as atribuições de variáveis
    symbols = {}

    # guardar as funções declaradas
    functions = {}

    # Defenir o que cada operador faz
    operators = {
        "+": lambda args: args[0] + args[1],
        "-": lambda args: args[0] - args[1],
        "*": lambda args: args[0] * args[1],
        "/": lambda args: args[0] / args[1],
        "seq": lambda args: args[-1],
        "string": lambda args: str(args[0]),
        "float": lambda args: float(args[0]),
        "int": lambda args: int(args[0]),
        "escrever": lambda args: print(args[0]),
        "atribuicao": lambda args: ArithEval._atribuicao(args),
        "comentario": lambda args: ArithEval._comentario(args),
        "concat": lambda args: f'{args[0]}{args[1]}',
        "interpolacao": lambda args: ''.join(args),
        "entrada": lambda args: ArithEval._entrada(args),
        "aleatorio": lambda args: ArithEval._aleatorio(args),
        "call_func": lambda args: ArithEval._call_func(args),
    }

    @staticmethod
    def _atribuicao(args):
        varid = args[0]  # 'A'
        value = args[1]  # 10
        ArithEval.symbols[varid] = value  # symbols { 'A':10 }
        #print(f'{varid}: {value}')
        return value

    @staticmethod
    def _comentario(args):
        return None

    @staticmethod
    def _entrada(args):
        return input("Função entrada, introduza o valor: ")

    @staticmethod
    def _aleatorio(args):
        maxNumero = int(args[0])
        if maxNumero <= 0:
            raise Exception("O valor do aleatorio tem de ser maior que 0")

        return random.randint(0, maxNumero)

    @staticmethod
    def _funcao(args, parametros, corpo):
        func_name = args[0]
        func_params = parametros
        func_body = corpo

        if func_name not in ArithEval.functions:
            ArithEval.functions[func_name] = []

        ArithEval.functions[func_name].append({
            'params': func_params,
            'body': func_body
        })

        return func_name

    @staticmethod
    def _call_func(args):
        func_name = args[0]
        call_params = args[1]

        if func_name not in ArithEval.functions:
            raise Exception(f"Função '{func_name}' não declarada")

        for func_def in ArithEval.functions[func_name]:
            func_params = func_def['params']
            func_body = func_def['body']

            if len(func_params) == len(call_params):
                # Salvar o estado atual de symbols
                previous_symbols = ArithEval.symbols.copy()

                # Adicionar parâmetros ao escopo atual
                local_symbols = previous_symbols.copy()
                for param, value in zip(func_params, call_params):
                    if 'var' in param:
                        local_symbols[param['var']] = ArithEval.evaluate(value)
                    elif 'op' in param and ArithEval.evaluate(param) == ArithEval.evaluate(value):
                        continue
                    else:
                        break
                else:
                    # Substituir temporariamente o escopo global com o escopo local
                    ArithEval.symbols = local_symbols
                    result = ArithEval.evaluate(func_body)

                    # Restaurar o estado anterior de symbols
                    ArithEval.symbols = previous_symbols
                    return result


        raise Exception(f"Nenhuma correspondência de parâmetros para a função '{func_name}'")

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return ArithEval._eval_operator(ast)
        if type(ast) is str:
            return ast
        if type(ast) is list:
            return [ArithEval.evaluate(a) for a in ast]
        raise Exception(f"Tipo de AST desconhecido {ast}")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast and ast['op'] == 'funcao':
            return ArithEval._funcao(ast['args'], ast['parametros'], ast['corpo'])

        if 'op' in ast:
            op = ast["op"]
            args = [ArithEval.evaluate(a) for a in ast['args']]
            if op in ArithEval.operators:
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Operador '{op}' desconhecido")

        if 'var' in ast:
            varid = ast["var"]  # ast={ 'var': "A" } =>   ast["var"]   varid="A"
            if varid in ArithEval.symbols:  # "A" in symbols { 'A':10 }
                return ArithEval.symbols[varid]  # 10
            raise Exception(f"error: '{varid}' não declarado (primeira utilização nesta função)")
        raise Exception('AST indefinido')
