from constructs import Construct
from aws_cdk import (
    Stage, App, Environment, Stage
)
import os
from .site_stack import StaticSiteStack

class StaticWebsitePipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = StaticSiteStack(self, "StaticSite")