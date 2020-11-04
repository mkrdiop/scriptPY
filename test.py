#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:10:23 2019

@author: makhtardiop
"""

# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = 'my-new-bucket'

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print('Bucket {} created.'.format(bucket.name))
