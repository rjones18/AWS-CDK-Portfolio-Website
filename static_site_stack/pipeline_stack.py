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

        secret_name = "snyk-key"
        snyk_secret = Secret.from_secret_name_v2(self, "ExistingSecretByName", secret_name)
        
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "master"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    'npm install -g snyk',
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    'snyk auth $SNYK_TOKEN',
                    "cdk synth",
                    'snyk iac test --report || echo "Snyk found vulnerabilities!"',
                ]
                env={
                        'SNYK_TOKEN': snyk_secret.secret_value.unsafe_unwrap()
                    }
            ),
        )

        deploy = StaticWebsitePipelineStage(self,"CloudFrontDeployment")
        deploy_stage = pipeline.add_stage(deploy)
