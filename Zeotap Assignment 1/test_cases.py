import unittest
from ast import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

    def test_combine_rules(self):
        rule1 = "age > 30 AND department = 'Sales'"
        rule2 = "salary > 50000"
        combined_ast = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_ast)

    def test_evaluate_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
