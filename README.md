# Professional Portfolio Backend

This repository hosts the backend files for my professional HTML portfolio web application hosted on AWS.

## Overview

This portfolio was modeled after the 'Cloud Resume Challenge' and serves as a personal website for use as my portfolio. This backend repository contains the assets required by my
visitor counter.

## Backend Flow
```
Website access --> API Gateway --> AWS Lambda(increment count and return total) --> API Gateway --> Website displays counter
```

## Features

- Entirely cloud hosted on AWS.
- HTML frontend entirely cloud hosted on an AWS S3 bucket. See the frontend explained in my [frontend repository](https://github.com/HarmonZ7/harmon-portfolio-frontend).
- API integration with AWS API gateway.
- AWS Lambda python script to increment and return persistent data present in AWS DynamoDB.
- Fully functional CI/CD with Github Actions updating and deploying live resources on AWS.
    - Workflow authenticates AWS access, then builds and deploys a SAM template which provisions and updates all my backend resources automatically.

## Tech Stack

- AWS API Gateway: Communicates website traffic to our lambda function.
- AWS Lambda: Increments persistent data and returns total number.
- AWS DynamoDB: Persistent data storage for our visitor counter
- AWS SAM: Abstraction above AWS Cloudformation, used for deploying AWS resources through a command line interface and YAML templates.
- AWS IAM Roles: Used to grant least privilege access to AWS services and Github actions to provision and deploy AWS services on my behalf.
- Python 3.13.7: Used for the Lambda script.
- Github: Used for repository management
  -Github Actions: Used for CI/CD in conjuction with SAM templates.

## Project Structure

```
harmon-portfolio-backend/
├── .github/
│   └── workflows/
│       └── main.yml
├── .aws-sam/
|   └── (contains SAM config files, condensed here for readability)  
├── visitor_counter/
|   ├── app.py
|   └── requirements.txt
├── template.yaml
└── README.md
```
