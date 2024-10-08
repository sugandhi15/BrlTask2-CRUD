from django.shortcuts import render
from taskcrud.models import addNote
from django.http import HttpResponse,JsonResponse
import json


# Create your views here.
def home(request):
    return HttpResponse(" Hello ")

#  \notes endpt request methods :-  GET,POST,DELETE 

def addnotes(request):

    # if we hit get request
    if request.method=='GET':
        try:
            data = addNote.objects.all().values()
            return HttpResponse(data)
        except Exception as e:
            return HttpResponse(e)
    

    # if we hit a post request
    if request.method=='POST':
        try:
            username=request.POST['username']
            email=request.POST['email']
            title=request.POST['title']
            desc=request.POST['desc']
            #  adding data to addNote
            note = addNote(username=username,email=email,title=title,desc=desc)
            note.save()
            return HttpResponse("saved")
        except Exception as e:
            return HttpResponse(e)


    # if request method is delete
    if request.method=='DELETE':
        try:
            addNote.objects.all().delete()
            return HttpResponse("Deleted data")
        except Exception as e:
            return HttpResponse(e)
    
    # to handle any other error 
    return HttpResponse("Error Occured")


# note/id to perform operation by passing id
def specificdata(request,param):
    
    # request method is get a specific note by id
    if request.method=='GET':
        try:
            data = addNote.objects.filter(id=param)
            if data.exists():
                return JsonResponse(list(data.values()), safe=False)
            else:
                return JsonResponse("Not Found")
        except Exception as e:
            return HttpResponse(e)
    
    # request to delete a specific note by id
    if request.method=='DELETE':
        try:
            if addNote.objects.filter(id=param):
                addNote.objects.filter(id=param).delete()
                return HttpResponse("Deleted Note successfully")
            else:
                return HttpResponse("No data found")
        except Exception as e:
            return HttpResponse(e)
        
    # to put data a specific data
    if request.method=='PUT':
        try:
            note = addNote.objects.filter(id=param).values()
            
            # Using json.loads to get PUT data from request body
            body = json.loads(request.body)
            
            note.username = body.get("username")
            note.email = body.get("email")
            note.title = body.get("title")
            note.desc = body.get("desc")
            
            note.save()
            return HttpResponse("Updated data successfully")
        except Exception as e:
            return HttpResponse(e)
            
    # to patch data
    if request.method=='PATCH':
        try:
            if addNote.objects.get(id=param):
                body = json.loads(request.body)
                # Update only provided fields
                if 'username' in body:
                    note.username = body.get('username')
                if 'email' in body:
                    note.email = body.get('email')
                if 'title' in body:
                    note.title = body.get('title')
                if 'desc' in body:
                    note.desc = body.get('desc')
                note.save()
                return JsonResponse('Note updated successfully')
            else:
                return HttpResponse("Note does not exist")
        except Exception as e:
            return HttpResponse(e)
    

def search(request,keyword):
    try:
        if request.method=='GET':
            try:
                data = addNote.objects.get(title=keyword)
                return JsonResponse(list(data.values()), safe=False)
            except Exception as e:
                return HttpResponse(e)
    except Exception as e:
        return HttpResponse(e)
    

