variable "vpc_id" {
  type = string
}

variable "public_subnet_ids" {
  type = list(string)
}

variable "app_security_group_id" {
  type = string
}

variable "instance_ids" {
  type = list(string)
}

variable "project_name" {
  type = string
} 