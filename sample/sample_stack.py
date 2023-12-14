from aws_cdk import Stack
from aws_cdk import aws_lambda
from constructs import Construct


class SampleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_code = aws_lambda.DockerImageCode.from_image_asset(
            directory=".", cmd=["sample.handler"]
        )
        aws_lambda.DockerImageFunction(
            scope=self, id="SampleFunction", code=lambda_code
        )
