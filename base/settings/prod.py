import os

from .base import *

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
USE_AWS = os.getenv("USE_AWS", "False") == "True"
if USE_AWS:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=604800, public, immutable"
    }  # 1 week
    AWS_DEFAULT_ACL = None
    AWS_S3_FILE_OVERWRITE = False
    AWS_IS_GZIPPED = True

    AWS_LOCATION = os.getenv("AWS_LOCATION")
    CLOUDFRONT_DOMAIN = os.getenv("AWS_CLOUDFRONT_DOMAIN")

    STATIC_URL = f"{CLOUDFRONT_DOMAIN}{AWS_LOCATION}/"
    STATICFILES_STORAGE = "storages.backends.s3.S3Storage"
else:
    STATIC_ROOT = BASE_DIR / "assets"
    STATIC_URL = "/static/"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# X_FRAME_OPTIONS = "ALLOW-FROM https://admin.shopify.com"
