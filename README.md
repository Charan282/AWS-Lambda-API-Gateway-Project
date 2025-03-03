# AWS-Lambda-API-Gateway-Project
# Overview
This project demonstrates how to create an API Gateway with multiple endpoints linked to AWS Lambda functions. It allows users to retrieve personal introduction details and a list of technical skills via API calls.

# Project Structure
# API Gateway: Acts as the front-end for the API, routing requests to appropriate Lambda functions.
# Lambda Functions: Two Lambda functions serve different responses.
Intro Function: Returns a personal introduction.
Skills Function: Returns a list of technical skills.

# Steps to Set Up
1. Create an API Gateway
Navigate to AWS API Gateway.
Create a Rest API.
2. Create and Configure Lambda Functions
First Lambda Function (Intro Function)
Second Lambda Function (skills)
3. Attach Lambda Functions to API Gateway
Attach the Intro Function to the / endpoint.
Attach the Skills Function to the /my-skills endpoint.
4. Deploy and Test the API
Deploy the API Gateway.
Copy the Invoke URL and test it in a browser:
{Invoke URL}/ → Returns introduction.
{Invoke URL}/my-skills → Returns skills list.
# Conclusion
This project demonstrates how to integrate AWS Lambda with API Gateway to serve dynamic content. It can be extended further by adding authentication, database connections, and additional endpoints.
