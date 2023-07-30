from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from api import serializers

from .models import Note
from .serializers import NoteSerializer
from .utils import *

# Create your views here.

@api_view(['GET','POST'])
def getNotes(request):
   if request.method =='GET':
      return getNotesList(request)
   
   if request.method == 'POST':
      return createNote(request)
    

    
@api_view(['GET','PUT','DELETE'])
def getNote(request, pk):
   if(request.method == 'GET'):
      return getNoteFromId(request, pk)
   
   elif(request.method =='PUT'):
      return updateNote(request, pk)
   
   elif(request.method=='DELETE'):
      return deleteNoteFromId(request, pk)




@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)
