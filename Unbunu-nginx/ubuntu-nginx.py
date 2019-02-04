from troposphere import Ref, Template,GetAtt, Parameter,FindInMap, Base64, Join,Output, Condition
import troposphere.ec2 as ec2
my_template = Template()

my_template.add_description(
    "Creates a Ubuntu 16.04 NGINX Web server in the current AWS region. based partly on https://github.com/widdix/learn-cloudformation/blob/master/lab2-parameters/sample-solution.yaml, last access 4/16/2018 && https://github.com/drpventura/cloud-formation/blob/master/simple-ubuntu-web2.yaml Last Access 01/17/2018 && https://anil.io/blog/aws/cloudformation/node-nginx-pm-template/")


def make_name(component_name):
    return '', [component_name, ' - ', Ref('AWS::StackName')]


parameters = {
    "One": Parameter(
        "VPC",
        Description="The default VPC",
        Type="AWS::EC2::VPC::Id"
    ),
    "Two": Parameter(
        "Subnet",
        Description="A public subnet from default VPC",
        Type="AWS::EC2::VPC::Id",
    ),
    "Three": Parameter(
        "KeyName",
        Description="Name of an existing EC2 KeyPair to enable SSH access to the instance",
        Type="AWS::EC2::KeyPair::KeyName",
        ConstraintDescription="must be the name of an existing EC2 KeyPair."
    ),
    "Four": Parameter(
        "SSHLocation",
        Description="The IP address range that can be used to SSH to the EC2 instances",
        Type="String",
        MinLength='9',
        MaxLength='18',
        Default="0.0.0.0/0",
        AllowedPattern='(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})',
        ConstraintDescription="must be a valid IP CIDR range of the form x.x.x.x/x."
    )
}

#Add security group
instanceSecurityGroup = my_template.add_resource(
    ec2.SecurityGroup(
        "WebserverSecurityGroup",
        GroupDescription="Hello World Web Server",
        SecurityGroupIngress=[
            # SSH
            ec2.SecurityGroupRule(IpProtocol='tcp', FromPort='22', ToPort='22', CidrIp=Ref(parameters['Four'])),

            # HTTP
            ec2.SecurityGroupRule(IpProtocol='tcp', FromPort='80', ToPort='80', CidrIp='0.0.0.0/0'),

            # HTTPS
            ec2.SecurityGroupRule(IpProtocol='tcp', FromPort='443', ToPort='443', CidrIp='0.0.0.0/0'),

            # Github - https://help.github.com/articles/what-ip-addresses-does-github-use-that-i-should-whitelist/
            # SecurityGroupRule(IpProtocol='tcp', FromPort='9418', ToPort='9418', CidrIp='192.30.252.0/22'),
        ],
        VpcId=Ref(parameters['One']),


    )
)
#create instance
ec2_instance = my_template.add_resource(ec2.Instance(
    "EC2Instance",
    ImageId=FindInMap("Region2AMI", Ref("AWS::Region"), "AMI"),
    InstanceType="t2.micro",
    KeyName=Ref(parameters['Three']),
    NetworkInterfaces=[
        ec2.NetworkInterfaceProperty(
            GroupSet=[
                Ref(instanceSecurityGroup)],
            AssociatePublicIpAddress='true',
            DeviceIndex='0',
            DeleteOnTermination='true',
            SubnetId=Ref(parameters['Two']))],

    UserData= Base64(
            Join(
            '',
            [
                '#!/bin/bash -xe',
                'sudo apt-get update',
                'sudo apt-get install curl -y',
                'sudo apt-get install nginx -y'
                'cd /var/www/html',
                'sudo chmod o+wx',
                'sudo chmod o+wx /var/www/html',
                'echo "html><title>The Index Page</title><body><h1>Robert Tessnow-Ramirez</h1><br><body" > index.html',
                'hostname=$(curl http://169.254.169.254/latest/meta-data/public-hostname)',
                'domain=$(curl http://169.254.169.254/latest/meta-data/services/domain)',
                'echo "<h1>The Public-hostname is"  $hostname "</h1><br>" >> index.html',
                'echo "<h1>The Domain is " $domain"</h1><br>" >> index.html'


            ]
        )
    )

))

for p in parameters.values():
    my_template.add_parameter(p)

my_template.add_mapping('Region2AMI', {
    #us-east-1 ohio from us-east-2 are for virginia
    "us-east-1": {"AMI": "ami-916f59f4"},
    "us-east-2": {"AMI": "ami-965e6bf3"},
    "us-west-1": {"AMI": "ami-07585467"},
    "us-west-2": {"AMI": "ami-79873901"},
    "ca-central-1": {"AMI": "ami-173db873"},
    "eu-central-1": {"AMI": "ami-5055cd3f"},
    "eu-west-1": {"AMI": "ami-1b791862"},
    "eu-west-2": {"AMI": "ami-941e04f0"},
    "eu-west-3": {"AMI": "ami-c1cf79bc"},
    "ap-northeast-1": {"AMI": "ami-48630c2e"},
    "ap-northeast-2": {"AMI": "ami-ab77d4c5"},
    "ap-southeast-1": {"AMI": "ami-b7f388cb"},
    "ap-southeast-2": {"AMI": "ami-33ab5251"},
    "ap-south-1": {"AMI": "ami-84e3b2eb"},
    "sa-east-1": {"AMI": "ami-bb9bd7d7"}
})

my_template.add_output([
    Output(
        "HelloWorldUrl",
        Description="The URL pointing to Hello World!.",
        Value= GetAtt(ec2_instance, "PublicDnsName")

    )
]
)


print(my_template.to_yaml())