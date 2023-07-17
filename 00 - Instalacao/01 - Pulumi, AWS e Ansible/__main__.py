"""An AWS Python Pulumi program"""
import pulumi
import configparser 
from pulumi_aws import ec2 

sg = ec2.SecurityGroup("securiyt-group-svc", description="Secure group for Jenkins")

allow_ssh = ec2.SecurityGroupRule("allow_ssh",
                            security_group_id=sg.id,
                            type="ingress",
                            from_port=22,
                            to_port=22,
                            protocol="tcp", 
                            cidr_blocks=["0.0.0.0/0"])

allow_http = ec2.SecurityGroupRule("allow_http",
                            security_group_id=sg.id,
                            type="ingress",
                            from_port=8080,
                            to_port=8080,
                            protocol="tcp",
                            cidr_blocks=["0.0.0.0/0"])

allow_external = ec2.SecurityGroupRule("allow_external",
                            security_group_id=sg.id,
                            type="egress",
                            from_port=0,
                            to_port=0,
                            protocol="-1",
                            cidr_blocks=["0.0.0.0/0"])


ec2_instance = ec2.Instance("jenkins", 
                            instance_type="t3.medium",
                            tags={"Name": "jenkins"},
                            key_name="homologacao",
                            ami="ami-053b0d53c279acc90",
                            vpc_security_group_ids=[sg.id])

pulumi.export('public_ip', ec2_instance.public_ip)
pulumi.export('instance_url', pulumi.Output.concat("http://", ec2_instance.public_dns, ":8080"))
