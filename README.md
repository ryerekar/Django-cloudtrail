# Django-cloudtrail
The current code is uploading files to a S3 bucket metnioned in the code on the AWS account. You can click on the choose File tba and select a file to be uploaded.

the second part of the code is creating a bucket in S3. you can enter a name and hit 'Create Bucket'

## Steps for deployment
  Place the folder on the desktop.
  
  pip install Django
  
  Update the access key in the seetings file: GitHub\Django-cloudtrail\cloudtrail\S3Project\settings.py
  
  On anaconda prompt navigate to the location where the folder is placed.
  run the command python manage.py runserver
  
  go to the web browser http://127.0.0.1:8000/ and test the code.
