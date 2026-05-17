from django.urls import path
from . views import Student_Crud, StudentView

urlpatterns = [
    path("students/",Student_Crud.as_view()),
    path("studentsview/",StudentView.as_view()),
    path("students/",Student_Crud.as_view()),
    # path("students/<int:ids>/",Student_Crud.as_view())

]
