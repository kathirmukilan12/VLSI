# Day 5 - Boolean Truth Table Generator

import itertools
import re


# --------------------------------------------------
# TOKENIZER
# --------------------------------------------------

def tokenize(expression):
    """
    Convert expression into tokens.

    Example:
        A AND (NOT B)

    becomes:
        ['A', 'AND', '(', 'NOT', 'B', ')']
    """

    pattern = r"\bAND\b|\bOR\b|\bNOT\b|\(|\)|[A-Za-z_][A-Za-z0-9_]*"

    tokens = re.findall(pattern, expression.upper())

    if not tokens:
        raise ValueError("Expression is empty.")

    return tokens


# --------------------------------------------------
# VARIABLES
# --------------------------------------------------

def get_variables(tokens):
    """Find variables in the expression."""

    operators = {"AND", "OR", "NOT"}

    variables = []

    for token in tokens:
        if token not in operators and token not in {"(", ")"}:
            if token not in variables:
                variables.append(token)

    return sorted(variables)


# --------------------------------------------------
# PARSER
# --------------------------------------------------

class Parser:

    def __init__(self, tokens, values):
        self.tokens = tokens
        self.values = values
        self.position = 0

    def current(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]

        return None

    def consume(self, expected=None):

        token = self.current()

        if token is None:
            raise ValueError("Unexpected end of expression.")

        if expected is not None and token != expected:
            raise ValueError(
                f"Expected {expected}, found {token}"
            )

        self.position += 1

        return token

    # OR has lowest precedence
    def parse_expression(self):

        result = self.parse_and()

        while self.current() == "OR":

            self.consume("OR")

            right = self.parse_and()

            result = result or right

        return result

    # AND has higher precedence than OR
    def parse_and(self):

        result = self.parse_not()

        while self.current() == "AND":

            self.consume("AND")

            right = self.parse_not()

            result = result and right

        return result

    # NOT has highest precedence
    def parse_not(self):

        if self.current() == "NOT":

            self.consume("NOT")

            return not self.parse_not()

        return self.parse_primary()

    # Variables and parentheses
    def parse_primary(self):

        token = self.current()

        if token == "(":

            self.consume("(")

            result = self.parse_expression()

            if self.current() != ")":
                raise ValueError("Missing closing parenthesis.")

            self.consume(")")

            return result

        if token in self.values:

            self.consume()

            return self.values[token]

        raise ValueError(f"Unexpected token: {token}")


# --------------------------------------------------
# EXPRESSION EVALUATION
# --------------------------------------------------

def evaluate_expression(expression, values):

    tokens = tokenize(expression)

    parser = Parser(tokens, values)

    result = parser.parse_expression()

    if parser.current() is not None:
        raise ValueError(
            f"Unexpected token: {parser.current()}"
        )

    return int(result)


# --------------------------------------------------
# TRUTH TABLE
# --------------------------------------------------

def generate_truth_table(expression):

    tokens = tokenize(expression)

    variables = get_variables(tokens)

    rows = []

    combinations = itertools.product([0, 1], repeat=len(variables))

    for combination in combinations:

        values = dict(zip(variables, combination))

        result = evaluate_expression(
            expression,
            values
        )

        row = values.copy()
        row["RESULT"] = result

        rows.append(row)

    return variables, rows


# --------------------------------------------------
# PRINT TABLE
# --------------------------------------------------

def print_truth_table(expression):

    variables, rows = generate_truth_table(expression)

    print()
    print("Expression:", expression)
    print("-" * 40)

    header = variables + ["RESULT"]

    print(" | ".join(f"{column:^8}" for column in header))

    print("-" * 40)

    for row in rows:

        values = [
            str(row[column])
            for column in header
        ]

        print(" | ".join(f"{value:^8}" for value in values))


# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":

    expressions = [
        "A AND B",
        "A OR B",
        "NOT A",
        "A AND (NOT B)",
        "(NOT A) OR B",
        "NOT (A AND B)",
        "NOT (A OR B)",
    ]

    for expression in expressions:
        print_truth_table(expression)