# AWS-CDK-Portfolio-Website
In this project, I utilized a suite of advanced AWS technologies to deploy a personal portfolio website. I utilized the AWS Python Cloud Development Kit (CDK) to define the AWS resources needed to host the website. To ensure continuous delivery, I leveraged CodePipeline and CodeCommit to automatically deploy any updates to the website.

For website hosting, I stored the website files in an S3 bucket and leveraged Amazon CloudFront to distribute the content globally with low latency. To provide a custom domain name, I configured Route 53 and integrated Amazon Certificate Manager to provide secure SSL/TLS encryption for the website.

On the frontend, I implemented the website using HTML, CSS, and JavaScript. By integrating this modern web technology stack with AWS's powerful cloud computing infrastructure, I was able to deploy a fast, scalable, and secure personal portfolio website.

Link to Website: https://rjportfoliosite.reggiestestdomain.com/

## Architecture Breakdown

The Website pipeline is broken down into the architecture below:

![portfolio](https://github.com/rjones18/Images/blob/main/Portfolio-Website-Pipeline-Diagram.png)
