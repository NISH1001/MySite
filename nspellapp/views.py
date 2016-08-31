from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status

import json

from .nspell import nspellwrapper

class API(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        data = request.GET
        text = nspellwrapper.run(data['text'])
        print(text)
        return Response(text)
        #return HttpResponse(json.dumps(data))

    def post(self, request, format=".json"):
        data = request.data
        text = nspellwrapper.run(data['text'][0])
        return Response(text)
