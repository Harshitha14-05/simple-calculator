class Calculator:
    @staticmethod
    def calculate(expression):
        """Evaluate a mathematical expression safely"""
        try:
            # Basic security check - only allow math operations
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                raise ValueError("Invalid characters in expression")
            
            # Evaluate the expression
            result = eval(expression, {'__builtins__': None}, {})
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero")
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")