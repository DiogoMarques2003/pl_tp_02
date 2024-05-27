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
