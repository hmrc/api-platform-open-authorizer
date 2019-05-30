# api-platform-application-authorizer

Lambda authorizer for open endpoints in the API platform. An authorizer is required here in order to override the standard Resource Policy present on the API.

## Dependencies

For production:
No requirements

For development/unit testing:
```bash
pip install -r requirements-dev.txt
```

## Development

To run/test the lambda function locally, install dependencies, then run:  
```bash
import lambda_function

lambda_function.lambda_handler(None, None)
```

## Tests

Install development dependencies, then

```bash
nosetests -v --with-cover --cover-erase --cover-package=lambda_function --cover-package=api_request_details --cover-package=validate_authorization_token
```

## Build

There is a `Jenkinsfile` which specifies the build pipeline. On successful build the lambda function zip artefact is
copied to an S3 bucket.
