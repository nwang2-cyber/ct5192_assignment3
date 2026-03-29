# CT5192 Assignment 3

This repository contains my work for Question 1 of CT5192 Assignment 3.

## Overview

In this task, I used Terraform to create a virtual machine on Google Cloud Platform (GCP).  
After that, I deployed a containerised frontend and backend application on the VM using Docker.  
I also set up logging and monitoring using:

- ELK stack (Elasticsearch + Kibana)
- New Relic

The goal was to show that the VM was created with Terraform, the application was running in containers, and logs from the frontend and backend could be viewed in the required monitoring tools.

## Repository structure

```text
ct5192_assignment3
├─ terraform
│  ├─ .terraform.lock.hcl
│  ├─ main.tf
│  ├─ variables.tf
│  └─ terraform.tfvars.example
│
├─ backend
│  ├─ app.py
│  ├─ Dockerfile
│  └─ .env.example
│
├─ screenshots
│  ├─ terraform-validate.png
│  ├─ terraform-apply-success.png
│  ├─ gcp-vm-instance-details.png
│  ├─ kibana-ui.png
│  ├─ kibana-frontend-logs.png
│  ├─ kibana-backend-logs.png
│  └─ newrelic-backend-logs.png
│
└─ README.md
```

## Terraform setup

Terraform was used to provision a VM instance on GCP.

Main Terraform files:

- `terraform/main.tf`
- `terraform/variables.tf`

A sample variables file is included:

- `terraform/terraform.tfvars.example`

The Terraform configuration was successfully validated before deployment.

## GCP virtual machine

A VM was created successfully on GCP using Terraform.

VM name used in this task:

- `ct5192-assignment3-vm`

The VM was then accessed through SSH in browser from Google Cloud Console.

## Containerised application

Two containers were used in this task.

### Frontend

A simple Nginx-based frontend was deployed and exposed on port 80.

### Backend

A simple Flask backend was deployed and exposed on port 5000.

The backend also generated log messages that were later used for monitoring in Kibana and New Relic.

## Logging with ELK

I deployed the following services on the VM using Docker:

- Elasticsearch
- Kibana
- Filebeat

Filebeat was configured to read Docker container log files for both frontend and backend containers and send them to Elasticsearch.

Kibana was exposed publicly and used to verify that:

- frontend logs were ingested
- backend logs were ingested

## Logging with New Relic

New Relic was used to verify backend log visibility.

A New Relic license key was configured through environment variables.  
Backend log messages containing `NEW_RELIC_LOG` were sent and then verified in the New Relic Logs UI.

## Important note

Sensitive files are **not included** in this repository.

These files were intentionally excluded:

- real `terraform.tfvars`
- real `.env`
- any real API key or license key
- Terraform state files
- local Terraform binaries

Example files are included instead:

- `terraform/terraform.tfvars.example`
- `backend/.env.example`

## Evidence

The `screenshots` folder contains the main evidence required for the task, including:

- Terraform validation output
- Terraform apply output
- GCP VM instance details
- Kibana UI
- Kibana frontend logs
- Kibana backend logs
- New Relic backend logs

## Summary

This task demonstrated:

- Infrastructure provisioning with Terraform
- VM deployment on GCP
- Containerised frontend and backend services using Docker
- Centralised logging with ELK
- Backend log visibility in New Relic
