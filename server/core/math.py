class MathExeciter:

    @classmethod
    def execute(cls, command):
        return eval(command["expression"])

    def _clean_data_for_response(cls, result, expression) :
        return {
            "given_math_expression": expression,
            "result": result
        }