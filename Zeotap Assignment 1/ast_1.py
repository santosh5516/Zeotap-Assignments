class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value      # For operands (e.g., age, department)
        self.left = left        # Left child (another Node)
        self.right = right      # Right child (another Node for operators)

import re

def create_rule(rule_string):
    tokens = re.split(r'(\(|\)|AND|OR|>|<|=| )', rule_string)
    tokens = [token.strip() for token in tokens if token.strip()]

    def build_ast(tokens):
        if not tokens:
            return None
        token = tokens.pop(0)
        if token == '(':
            left = build_ast(tokens)
            operator = tokens.pop(0)
            right = build_ast(tokens)
            tokens.pop(0)  # Pop closing ')'
            return Node("operator", operator, left, right)
        elif re.match(r'\d+|[a-zA-Z]+', token):
            return Node("operand", token)

    return build_ast(tokens)

def combine_rules(rules):
    combined_ast = None
    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node("operator", "AND", combined_ast, ast)
    return combined_ast

def evaluate_rule(ast, data):
    if ast.type == "operand":
        return data.get(ast.value)
    elif ast.type == "operator":
        left_val = evaluate_rule(ast.left, data)
        right_val = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_val and right_val
        elif ast.value == "OR":
            return left_val or right_val
