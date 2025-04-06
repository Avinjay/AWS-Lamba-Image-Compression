import boto3
import os
from PIL import Image
import tempfile

s3 = boto3.client('s3')

DEST_BUCKET = 'avinjay-bacth10'  # Your destination bucket

def lambda_handler(event, context):
    print("Event received:", event)

    if 'Records' not in event:
        return {
            'statusCode': 400,
            'body': 'No S3 event detected.'
        }

    try:
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"Object key: {key}, from bucket: {source_bucket}")

        download_path = os.path.join(tempfile.gettempdir(), os.path.basename(key))
        compressed_key = f"compressed-{os.path.basename(key)}"
        compressed_path = os.path.join(tempfile.gettempdir(), compressed_key)

        print(f"Downloading {key} from {source_bucket}")
        s3.download_file(source_bucket, key, download_path)

        # Compress image
        with Image.open(download_path) as img:
            print(f"Compressing image: {key}")
            img = img.convert("RGB")  # Avoid PNG mode issues
            img.save(compressed_path, optimize=True, quality=60)

        print(f"Uploading compressed image as {compressed_key} to {DEST_BUCKET}")
        s3.upload_file(compressed_path, DEST_BUCKET, compressed_key)

        print("Upload complete.")
        return {
            'statusCode': 200,
            'body': f'Compressed image saved to {DEST_BUCKET}/{compressed_key}'
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
