import base64
from modules.s3 import s3_client
from urllib.parse import urlparse


def get_photo_base64(s3_url) -> str:
    try:
        s3_url = s3_url
        parsed = urlparse(s3_url)
        path_parts = parsed.path.lstrip('/').split('/', 1)

        if len(path_parts) != 2:
            raise ValueError("Не удалось извлечь bucket и key из URL.")

        bucket_name, s3_key = path_parts

        response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
        image_data = response['Body'].read()
        return base64.b64encode(image_data).decode('utf-8')
    except Exception as e:
        print(f"Ошибка при получении файла: {e}")
        return ""
