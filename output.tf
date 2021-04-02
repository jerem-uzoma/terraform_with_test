output "main_vpc_id" {
  value       = aws_vpc.main.id
  description = "The main VPC id"
}

output "public_subnet_id" {
  value       = aws_subnet.public.id
  description = "The public subnet id"
}

output "private_subnet_id" {
  value       = aws_subnet.private.id
  description = "The private subnet id"
}

output "main_vpc_name" {
  value       = lookup(module.vpc.tags, "Name")
  description = "The VPC name"
}
output "main_vpc_cidr" {
  value = aws_vpc.main.cidr_block
}
