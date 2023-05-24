from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.template.response import TemplateResponse
import os, os.path

# Create your views here.

def testStream(request):
    #template = loader.get_template(settings.TEMPLATES[0]['DIRS'][0])
    template = loader.get_template('testStream.html')
    template3 = loader.get_template('testStream2.html')
    streamFile = os.path.join(settings.STREAM_DIR, 'stream.m3u8')
    streamFile = os.path.join(settings.STREAM_DIR, 'index.html')
    #streamFileOutput = os.path.join(settings.STREAMFILE_DIR, 'stream.m3u8')
    #streamFileOutput = os.path.join(settings.STREAMFILE_DIR, 'stream.m3u8')
    template2 = loader.get_template(streamFile)

    print(streamFile)
    context = {
            'streamFileOutput' : 'poopy',
            }

#    return HttpResponse(template.render())

    return TemplateResponse(request, 'testStream.html', {})


