class MathExecuter:

    @classmethod
    async def execute(cls, command: dict) -> dict:
        expression = command["expression"]
        result = await cls._async_eval(expression)
        response = await cls._clean_data_for_response(result, expression)

        return response

    @classmethod
    async def _async_eval(cls, expression) :
        return eval(expression)

    @classmethod
    async def _clean_data_for_response(cls, result: float, expression: str) -> dict:
        return {
            "given_math_expression": expression,
            "result": result
        }