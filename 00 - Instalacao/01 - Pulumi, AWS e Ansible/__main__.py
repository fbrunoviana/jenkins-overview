"""An AWS Python Pulumi program"""
import pulumi
from pulumi_aws import ec2, s3 

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

sg = ec2.SecurityGroup('web-svc-gro', description="Security group for web service")

allow_ssh = ec2.SecurityGroupRule("AllowSSH", type="ingress", 
                                  from_port=22, to_port=22, 
                                  protocol="tcp", 
                                  cidr_blocks=["0.0.0.0/0"], 
                                  security_group_id=sg.id)

allow_http = ec2.SecurityGroupRule("AllowHTTP", type="ingress",
                                   from_port=8080, to_port=8080,
                                   protocol="tcp",
                                   cidr_blocks=["0.0.0.0/0"], 
                                   security_group_id=sg.id)

allow_all = ec2.SecurityGroupRule("AllowALL", type="egress",
                                  from_port=0, to_port=0,
                                  protocol="-1",
                                  cidr_blocks=["0.0.0.0/0"],
                                  security_group_id=sg.id)


ec2_instance = ec2.Instance("jenkins", 
                            instance_type="t3.medium",
                            tags={"Name": "jenkins"},
                            key_name="homologacao",
                            ami="ami-053b0d53c279acc90",
                            vpc_security_group_ids=[sg.id])

pulumi.export('public_ip', ec2_instance.public_ip)
pulumi.export('instance_url', pulumi.Output.concat("http://", ec2_instance.public_dns, ":8080"))