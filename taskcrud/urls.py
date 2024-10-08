from django.urls import path
from . import views

urlpatterns = [
    #  to get home page
    path("",views.home,name="homepage"),
    # \notes endpt to add , read and delete note
    path("notes",views.addnotes,name="addnotes"), 
    # \to get specific notes like:- get by note id,delete by note id
    path("note/<int:param>",views.specificdata,name="specificdata"),
    # to search data by keyword 
    path("note/search/<str:keyword>",views.search,name="search"),
    # to get recent note
    # path("note/recent",views.recent,name="recent")
]
