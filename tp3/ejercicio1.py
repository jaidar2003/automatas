class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)


# Parsing Table
table = {
    ('E', 'id'): ['T', "E'"],
    ('E', '('): ['T', "E'"],
    ("E'", '+'): ['+', 'T', "E'"],
    ("E'", '-'): ['-', 'T', "E'"],
    ("E'", '%'): ['%', 'T', "E'"],
    ("E'", ')'): ['ε'],
    ("E'", '$'): ['ε'],
    ('T', 'id'): ['id'],
    ('T', '('): ['(', 'E', ')']
}

def parse(input_tokens):
    input_tokens.append('$')

    stack = Stack()
    stack.push('$')
    stack.push('E')

    index = 0
    symbol = input_tokens[index]

    while not stack.is_empty():
        top = stack.top()
        if top == symbol:
            stack.pop()
            index += 1
            symbol = input_tokens[index]
        elif (top, symbol) in table:
            stack.pop()
            production = table[(top, symbol)]
            if production != ['ε']:
                for item in reversed(production):
                    stack.push(item)
        else:
            return False
    return True

# Calculate the result for a valid expression
def evaluate(expression):
    import operator
    import re

    # Define operator precedence and corresponding operations
    precedence = {'+': 1, '-': 1, '%': 2}
    operators = {'+': operator.add, '-': operator.sub, '%': operator.mod}

    def parse_expression(expression):
        tokens = re.findall(r'\d+|\+|\-|\%|\(|\)', expression)
        return tokens

    def infix_to_postfix(tokens):
        output = []
        stack = []
        for token in tokens:
            if token.isdigit():
                output.append(int(token))
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while stack and stack[-1] in precedence and precedence[token] <= precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate_postfix(postfix_tokens):
        stack = []
        for token in postfix_tokens:
            if isinstance(token, int):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a, b))
        return stack[0]

    tokens = parse_expression(expression)
    postfix_tokens = infix_to_postfix(tokens)
    return evaluate_postfix(postfix_tokens)


if __name__ == "__main__":
    expr = "10+5-2"
    tokens = parse_expression(expr)
    if parse(tokens):
        result = evaluate(expr)
        print(f"The result of the expression '{expr}' is: {result}")
    else:
        print("Syntax Error: The expression is invalid.")
