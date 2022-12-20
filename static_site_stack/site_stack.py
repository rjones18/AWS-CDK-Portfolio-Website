from aws_cdk import ( 
    Stack, 
    aws_cloudfront_origins, 
    aws_cloudfront, 
    aws_s3,
    aws_route53,
    aws_certificatemanager,
    aws_s3_deployment
)


class StaticSiteStack(Stack):
    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        # Create S3 bucket for Cloudfront to point to
        bucket = aws_s3.Bucket(
            self, f"Cloufrontbucket",
            bucket_name="rjportfoliowebsitebucket",
            encryption=aws_s3.BucketEncryption.S3_MANAGED,
            block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True, 
    )
        

        # Reference Route 53 DNS Zone
        zone = aws_route53.HostedZone.from_hosted_zone_attributes(self, "MyZone",
        zone_name="reggiestestdomain.com",
        hosted_zone_id="Z03743244DPHU4YSX41G"
)

        #Create Certificate for SSL
        certificate = aws_certificatemanager.Certificate(self, "Certificate",
                      domain_name="rjportfoliosite.reggiestestdomain.com",
                      validation=aws_certificatemanager.CertificateValidation.from_dns(zone)
)



        # Creates a distribution from an S3 bucket.
        distribution = aws_cloudfront.Distribution(
            self,
            "cloudfront_distribution",
            default_behavior=aws_cloudfront.BehaviorOptions(
                origin=aws_cloudfront_origins.S3Origin(bucket),
                viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            domain_names=["rjportfoliosite.reggiestestdomain.com"],
            certificate=certificate,
            default_root_object="index.html",
        )
        

        # Create Route53 A Record for Cloudfront distribution       
        aws_route53.CnameRecord (self, "Alias",
                    record_name="rjportfoliosite",
                    zone=zone,
                    domain_name=distribution.domain_name
             
             )

        #Deploys the websites code into the S3 Bucket   
        aws_s3_deployment.BucketDeployment(self, "DeployWebsite",
                 sources=[aws_s3_deployment.Source.asset("./website_contents")],
                 destination_bucket=bucket,
                 #destination_key_prefix="./"
                 
            )