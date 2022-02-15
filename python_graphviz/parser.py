import sys
import re
import logging

py_regex = r'{{( |[= ]|\n)[^{}]+( |\n)}}'


def convert(python_graphviz: str) -> str:
    """
    Convert python graphviz to graphviz
    """

    python_codes = re.finditer(py_regex, python_graphviz)
    position_correction = 0

    for code in python_codes:
        expression = code.group()
        variable = expression[2] == '='

        py_code = expression[4 if variable else 3:-3]

        try:
            if variable:
                output = eval(py_code)

                has_decimal_places = type(output) == float

                if not has_decimal_places:
                    try:
                        import numpy as np
                        has_decimal_places = type(output) == np.float64
                    except ImportError:
                        pass

                if has_decimal_places:
                    r = 2
                    try:
                        r = round_digits
                    except NameError:
                        pass

                    num = float(output)
                    output = round(num, r)

                    logging.debug(f"Rounded {num} to output")

                output = str(output)
            else:
                exec(py_code)
                output = ""
        except Exception as ex:
            raise Exception(f"Error while processing: {expression}", ex)

        python_graphviz = f"{python_graphviz[:code.start() + position_correction]}{output}{python_graphviz[code.end() + position_correction:]}"

        position_correction = position_correction + (len(output) - len(expression))

        if variable:
            logging.debug(f"Executing with output: {expression} ⟶ {output}")
        else:
            logging.debug(f"Executing without output: {expression}")

    # Clear all variables
    sys.modules[__name__].__dict__.clear()

    return python_graphviz
