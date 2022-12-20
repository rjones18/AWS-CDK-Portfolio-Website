#!/usr/bin/env python3

import aws_cdk as cdk
from static_site_stack.pipeline_stack import PortfolioPipelineStack


app = cdk.App()
PortfolioPipelineStack(app, "PortfolioWebsitePipelineStack")

app.synth()