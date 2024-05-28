# arith_eval

class ArithEval:
    # guardar as atribuições de variáveis
    symbols = {}

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
    }

    @staticmethod
    def evaluate(ast):
        if type(ast) is int:  # constant value, eg in (int, str)
            return ast
        if type(ast) is dict:  # { 'op': ... , 'args': ...}
            return ArithEval._eval_operator(ast)
        if type(ast) is str:
            return ast
        raise Exception(f"Unknown AST type")

    @staticmethod
    def _eval_operator(ast):
        if 'op' in ast:
            op = ast["op"]
            args = [ArithEval.evaluate(a) for a in ast['args']]
            if op in ArithEval.operators:
                func = ArithEval.operators[op]
                return func(args)
            else:
                raise Exception(f"Unknown operator {op}")

        if 'var' in ast:
            varid = ast["var"]  # ast={ 'var': "A" } =>   ast["var"]   varid="A"
            if varid in ArithEval.symbols:  # "A" in symbols { 'A':10 }
                return ArithEval.symbols[varid]  # 10
            raise Exception(f"error: '{varid}' undeclared (first use in this function)")
        raise Exception('Undefined AST')
