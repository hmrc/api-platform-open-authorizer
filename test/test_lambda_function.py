import unittest
import lambda_function


class TestLambdaFunction(unittest.TestCase):

    def test_correctly_produces_policy_from_valid_request(self):
        method = "GET"
        path = "/hello/world"
        method_arn = "arn:aws:execute-api:eu-west-2:123456789012:abcde123/current/{}{}".format(method, path)

        lambda_event = self.create_lambda_authorization_event(method, path, method_arn)
        lambda_context = self.create_lambda_context()

        generated_policy = lambda_function.lambda_handler(lambda_event, lambda_context)
        generated_policy_document = generated_policy["policyDocument"]
        generated_statement = generated_policy_document["Statement"][0]
        generated_resource = generated_statement["Resource"][0]

        self.assertEqual("2012-10-17", generated_policy_document["Version"])

        self.assertEqual("execute-api:Invoke", generated_statement["Action"])
        self.assertEqual("Allow", generated_statement["Effect"])

        self.assertEqual(method_arn, generated_resource)

    @staticmethod
    def create_lambda_authorization_event(method, path, method_arn):
        return {
            "type": "REQUEST",
            "methodArn": method_arn,
            "path": path,
            "httpMethod": method
        }

    @staticmethod
    def create_lambda_context():
        return {}
