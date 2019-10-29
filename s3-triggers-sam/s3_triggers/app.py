import json

import requests
import boto3
import logging
import os
import uuid

# Add to path so that Layers can be imported
import sys
#sys.path.insert(0, '/opt')
from PIL import Image
import PIL.ImageOps


s3_client = boto3.client('s3')
dest_bucket = os.environ['DestBucket']


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        logging.info("resizing...")
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(resized_path)


def invert_image(image_path, inverted_path):
    with Image.open(image_path) as image:
        logging.info("inverting...")
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save(inverted_path)


def lambda_handler(event, context):
    logging.info(event)
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/inverted-{}'.format(key)
        s3_client.download_file(bucket, key, download_path)
        invert_image(download_path, upload_path)
        s3_client.upload_file(upload_path, dest_bucket, 'inverted-{}'.format(key))

        # just for debug
        summary = dict(download_path=download_path, upload_path=upload_file, bucket=bucket, key=key)
        json.dumps(summary, indent=2, sort_keys=True)
        return summary
