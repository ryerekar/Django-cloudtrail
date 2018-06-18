# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#from django.core.urlresolvers  import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Document
import boto3
from django.conf import settings
import botocore


# Create your views here.
class DocumentCreateView(CreateView):
    model = Document
    fields = ('upload',)
    success_url = reverse_lazy('upload')

def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		documents = Document.objects.all()
		context['documents'] = documents
		return context

def return_data(request):
    try:
        createBucket(request.POST['bucket'])
        return HttpResponse('Bucket created successfully')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyExists':
            return HttpResponse("Cannot create the bucket. A bucket with the name " + request.POST['bucket'] + " already exists.")




#def createBucket(bucketName):
 #   s3 = boto3.resource('s3', aws_access_key_id=getattr(settings, "AWS_ACCESS_KEY_ID", None),
  #       aws_secret_access_key= getattr(settings, "AWS_SECRET_ACCESS_KEY", None))
   # s3.create_bucket(Bucket=bucketName)


def createBucket(bucketName):
    s3 = boto3.resource('s3', aws_access_key_id=getattr(settings, 'AWS_ACCESS_KEY_ID', None),
                        aws_secret_access_key=getattr(settings, 'AWS_SECRET_ACCESS_KEY', None))
    s3.create_bucket(Bucket=bucketName)


def return_logs(request):
    return render(request,)