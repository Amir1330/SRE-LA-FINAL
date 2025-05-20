provider "aws" {
  region = "us-west-2"
}

# VPC and networking
module "vpc" {
  source = "modules/vpc"
  
  vpc_cidr_block = "10.0.0.0/16"
  project_name   = "sre-demo"
}

# EC2 instances for the application
module "compute" {
  source = "modules/compute"
  
  instance_count = 2
  vpc_id         = module.vpc.vpc_id
  subnet_ids     = module.vpc.public_subnet_ids
  project_name   = "sre-demo"
}

# Security groups
module "security" {
  source = "modules/security"
  
  vpc_id       = module.vpc.vpc_id
  project_name = "sre-demo"
}

# Load balancing
module "lb" {
  source = "modules/lb"
  
  vpc_id                = module.vpc.vpc_id
  public_subnet_ids     = module.vpc.public_subnet_ids
  app_security_group_id = module.security.app_security_group_id
  instance_ids          = module.compute.instance_ids
  project_name          = "sre-demo"
}

# Monitoring resources
module "monitoring" {
  source = "modules/monitoring"
  
  vpc_id                = module.vpc.vpc_id
  subnet_ids            = module.vpc.public_subnet_ids
  app_security_group_id = module.security.app_security_group_id
  project_name          = "sre-demo"
} 