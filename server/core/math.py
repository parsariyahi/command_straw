class MathExeciter:

    @classmethod
    def execute(cls, command: dict) -> dict:
        expression = command["expression"]
        result = eval(expression)

        return cls._clean_data_for_response(result, expression)

    @classmethod
    def _clean_data_for_response(cls, result: float, expression: str) -> dict:
        return {
            "given_math_expression": expression,
            "result": result
        }