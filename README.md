# Pixel_Learning_Company1
This repository is for the Pixel Learning Co for audio content
This is an overview to use AWS polly to convert text input into an MP3 audio file, then the process is automated with a Python Script and GitHub Actions 

## Instructions for Setup

## AWS Credentials Setup
First, setup the AWS Credentials Setup

Create a '.env' filew with following variables:

```env
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
S3_BUCKET_NAME=your-s3-bucket-name

Once the file is created, use this file within the Python script with the os.environ method to authenciate with AWS and access the S3 Bucket.

## Modify the text for Amazon Polly
Create a "speech.txt" file that has the text input for Amazon Polly. Once this is updated, make that this file is save in the same directory as the python script.
Ensure that the text file is properly commited and tracked in GitHub with no hidden extensions to the file.

## Run the python script synthensize.py
The script will read the speech.txt, synthesize the speech with AWS Polly.
Save the file under a unique name (e.g., Pixel_Learning.MP3)
Upload to MP3 to specified S3 Bucket

## GitHub Actions Workflow
Trigger Conditions
Use GitHub Action to trigger the python script:
-'.github/workflows/synthesize.yml' is set to run on:
  -'push' event to 'main' branch
  -'pull_request'events

The workflow sets up Python, install dependenceies, load the '.env.example" using 'python-doteven', and run the Python Script.

## Verify Uplaods to S3 Bucket
Log into the AWS Console
Navigate to the S3 console and open the specified bucket
Go to the uploaded object
Download and play to ensure it is working properly.
