from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
)
from static_site_stack.pipeline_stage import StaticWebsitePipelineStage

class PortfolioPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeCommit repository
        repo = codecommit.Repository(
            self, "Portfolio-Website", repository_name="Portfolio-Website-Pipeline"
        )
        
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "master"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ]
            ),
        )

        deploy = StaticWebsitePipelineStage(self,"CloudFrontDeployment")
        deploy_stage = pipeline.add_stage(deploy)