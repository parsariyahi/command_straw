from .base import Executer


class MathExecuter(Executer):
    """
    An executer class for evaluating mathematical expressions.
    """

    @classmethod
    async def execute(cls, command: dict) -> dict:
        """
        Evaluate the specified mathematical expression and return the result.

        Args:
            command (dict): A dictionary representing the command to execute.

        Returns:
            A dictionary representing the result of the command execution.
        """
        expression = command["expression"]
        result = await cls._async_eval(expression)
        response = await cls._clean_data_for_response(result, expression)

        return response

    @classmethod
    async def _async_eval(cls, expression: str) -> float:
        """
        Evaluate the specified mathematical expression using the built-in Python eval function.

        Args:
            expression (str): The mathematical expression to evaluate.

        Returns:
            The result of evaluating the expression as a floating point number.
        """
        return eval(expression)

    @classmethod
    async def _clean_data_for_response(cls, result: float, expression: str) -> dict:
        """
        Clean up the input and output data and return them as a dictionary.

        Args:
            result (float): The result of evaluating the mathematical expression.
            expression (str): The original mathematical expression that was evaluated.

        Returns:
            A dictionary containing the cleaned up input and output data.
        """
        return {
            "given_math_expression": expression,
            "result": result
        }
