import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def synthesize_speech(text_file_path, output_file):
    with open(text_file_path, 'r') as file: 
        text = file.read()

    #Start Amazon Polly
    polly = boto3.client('polly', region_name='us-east-1')

    #Synthesize the speech
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId= 'Matthew'
    )

    #Save audio to MP3
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())
        
        print("Save MP3 file as Pixel_Learning.mp3")

def upload_to_s3(file_name,object_name=None):
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket_name = os.environ['S3_BUCKET_NAME']
    s3.upload_file(file_name, bucket_name, file_name)

    print(f"Upload {'Pixel_Learning.mp3'} to s3://[pixellearningpolly ]/[polly-audio.Pixel.Learning.mp3]")

if __name__ == "__main__":
    synthesize_speech("speech.txt", "Pixel_Learning.mp3")
    upload_to_s3("Pixel_Learning.mp3", "Pixel_Learning.mp3")

