from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class StaticRootS3BotoStorage(S3Boto3Storage):
    # AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % settings.AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    location = 'static_new'
# StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
# MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='products')
#
class MediaRootS3BotoStorage(S3Boto3Storage):
    # AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % settings.AWS_STORAGE_BUCKET_NAME
    location = 'products_new'
    AWS_DEFAULT_ACL = None
    file_overwrite = False