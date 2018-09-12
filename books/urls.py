from django.urls import path
from .views import BookList, SummaryList,Generatepdf

urlpatterns = [
path('', BookList.as_view()),
path('<int:pk>/', SummaryList.as_view()),
path('1/pdf', Generatepdf.as_view())
]
