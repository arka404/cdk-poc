from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from constructs import Construct

class CdkPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, id="First-cdk-bucket", bucket_name="my-blue-bucket-4", versioned=True)
