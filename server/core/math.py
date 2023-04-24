class MathExeciter:

    @classmethod
    def execute(cls, expression):
        return eval(expression)

    def _clean_data_for_response(cls, result, expression) :
        return {
            "given_math_expression": expression,
            "result": result
        }