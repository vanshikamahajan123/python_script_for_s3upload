#!/usr/bin/env python
import boto3,os

def s3_file_upload(path, bucket_name, bucket_prefix):
    s3 = boto3.client('s3')
    files = os.listdir(path)
    print files
    for upload_file in files:
        local_file = path + "/" + upload_file
        s3_key = bucket_prefix + upload_file

        try:
            print "Starting Uploading %s file to s3"%local_file
            s3.upload_file(local_file, bucket_name, s3_key)
            print "Successfully uploaded %s file to %s"%(local_file,s3_key)
        except:
            print "%s failed to upload bucket=%s to s3 folder=%s"%(local_file,bucket_name,s3_key)

s3_file_upload("/home/vanshika/upload","python-work","data/")