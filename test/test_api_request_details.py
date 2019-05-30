import unittest
from api_request_details import ApiRequestDetails


class TestApiRequestDetails(unittest.TestCase):

    def test_correctly_parses_arn(self):
        aws_region = "eu-west-2"
        aws_account_number = "123456789012"
        aws_rest_api_id = "abcde123"
        aws_rest_api_stage_name = "current"
        request_method = "GET"
        request_path = "/hello"

        method_arn = "arn:aws:execute-api:{}:{}:{}/{}/{}{}"\
            .format(aws_region, aws_account_number, aws_rest_api_id, aws_rest_api_stage_name, request_method, request_path)

        api_request_details = ApiRequestDetails(method_arn)

        self.assertEqual(aws_region, api_request_details.aws_region)
        self.assertEqual(aws_account_number, api_request_details.aws_account_number)
        self.assertEqual(aws_rest_api_id, api_request_details.rest_api_id)
        self.assertEqual(aws_rest_api_stage_name, api_request_details.stage)
        self.assertEqual(request_method, api_request_details.method)
        self.assertEqual(request_path, api_request_details.path)

    def test_correctly_parses_arn_with_multi_stage_path(self):
        aws_region = "eu-west-2"
        aws_account_number = "123456789012"
        aws_rest_api_id = "abcde123"
        aws_rest_api_stage_name = "current"
        request_method = "GET"
        request_path = "/hello/world"

        method_arn = "arn:aws:execute-api:{}:{}:{}/{}/{}{}"\
            .format(aws_region, aws_account_number, aws_rest_api_id, aws_rest_api_stage_name, request_method, request_path)

        api_request_details = ApiRequestDetails(method_arn)

        self.assertEqual(aws_region, api_request_details.aws_region)
        self.assertEqual(aws_account_number, api_request_details.aws_account_number)
        self.assertEqual(aws_rest_api_id, api_request_details.rest_api_id)
        self.assertEqual(aws_rest_api_stage_name, api_request_details.stage)
        self.assertEqual(request_method, api_request_details.method)
        self.assertEqual(request_path, api_request_details.path)
