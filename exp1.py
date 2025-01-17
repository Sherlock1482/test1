import re
# Input expression
exp = input("Enter an expression: ")
# Tokenize the expression using regular expressions
tokens = re.findall(r'\w+|[+\-*/;]|=|\d+', exp)
# Initialize counters for each type of token
identifier_count = 1
constant_count = 1
operator_count = 1
assignment_count = 1
delimiter_count = 1
# Categorize and print tokens with unique incrementing labels
for token in tokens:
    if token.isdigit():
        print(f"{token}: Constant_{constant_count}")
        constant_count += 1
    elif token.isidentifier():
        print(f"{token}: Identifier_{identifier_count}")
        identifier_count += 1
    elif token in ['+', '-', '*', '/']:
        print(f"{token}: Operator_{operator_count}")
        operator_count += 1
    elif token == ';':
        print(f"{token}: Delimiter_{delimiter_count}")
        delimiter_count += 1
    elif token == '=':
        print(f"{token}: Assignment_{assignment_count}")
        assignment_count += 1
    else:
        print(f"{token}: Unknown")
