import boto3
from botocore.exceptions import ClientError
from app.config import get_settings
import uuid
from typing import Optional

settings = get_settings()

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION
        )
        self.bucket = settings.AWS_S3_BUCKET
        self.base_url = settings.AWS_S3_BASE_URL

    def upload_image(self, image_data: bytes, content_type: str) -> Optional[str]:
        """
        Upload an image to S3 and return its URL
        """
        try:
            # Generate a unique filename
            file_extension = content_type.split('/')[-1]
            filename = f"{uuid.uuid4()}.{file_extension}"
            
            # Upload to S3
            self.s3_client.put_object(
                Bucket=self.bucket,
                Key=filename,
                Body=image_data,
                ContentType=content_type,
                ACL='public-read'  # Make the image publicly accessible
            )
            
            # Return the public URL
            return f"{self.base_url}/{filename}"
        except ClientError as e:
            print(f"Error uploading to S3: {e}")
            return None

    def delete_image(self, image_url: str) -> bool:
        """
        Delete an image from S3
        """
        try:
            # Extract the filename from the URL
            filename = image_url.split('/')[-1]
            
            # Delete from S3
            self.s3_client.delete_object(
                Bucket=self.bucket,
                Key=filename
            )
            return True
        except ClientError as e:
            print(f"Error deleting from S3: {e}")
            return False

# Create a singleton instance
s3_service = S3Service() 