import re


class ApiRequestDetails:

    aws_region = ""
    aws_account_number = ""
    rest_api_id = ""
    stage = ""
    method = ""
    path = ""

    def __init__(self, method_arn):
        method_arn_regex = "arn:aws:execute-api:(.*):([0-9]{12}):([a-z0-9]*)/(.*)/(GET|POST|PUT|DELETE)(.*)"

        match = re.search(method_arn_regex, method_arn)

        if match:
            self.aws_region = match.group(1)
            self.aws_account_number = match.group(2)
            self.rest_api_id = match.group(3)
            self.stage = match.group(4)
            self.method = match.group(5)
            self.path = match.group(6)
        else:
            raise Exception("Unable to parse API Gateway Method ARN: {}", method_arn)
