import boto3
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        kwargs = {
            'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
            'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
            'region_name': settings.AWS_S3_REGION_NAME,
        }

        bucket_name = 'dragaliagg'
        object_name = 'dragaliagg-db-backup.sql'
        db_file_path = '/tmp/dragaliagg-db-backup.sql'

        s3 = boto3.client('s3', **kwargs)
        last_updated = s3.get_object(Bucket=bucket_name, Key=object_name)['LastModified']

        answer = input('Restore Database from S3, last updated {0}? [Y/N] '.format(last_updated))

        if answer == 'Y':
            print('# Downloading DB Dump')
            s3.download_file(bucket_name, object_name, db_file_path)
            print('# Importing DB Dump')
            os.system('mysql -h{0} -u{1} -p{2} --database={3} < {4}'.format(
                settings.DATABASES['default']['HOST'],
                settings.DATABASES['default']['USER'],
                settings.DATABASES['default']['PASSWORD'],
                settings.DATABASES['default']['NAME'],
                db_file_path
            ))
            print('# Removing DB File')
            os.remove(db_file_path)

        else:
            raise CommandError('OKbye.')
