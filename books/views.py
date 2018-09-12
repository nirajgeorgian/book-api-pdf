from .utils import pdf_generator
from django.http import HttpResponse
from rest_framework import generics
from .models import Book,Summary
from django.views import generic
from .serializers import BookSerializer,SummarySerializer
from django.template.loader import get_template


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SummaryList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class Generatepdf(generic.ListView):

    def get(self,request,*args,**kwargs):
        all_books = Book.objects.all()
        print(all_books)
        template = get_template("index.html")
        context = {
        'all_books':all_books,
        }
        html = template.render(context)
        print(html)
        pdf = pdf_generator('index.html',context)
        if pdf:
            return HttpResponse(pdf,content_type="application/pdf")
        return HttpResponse("not found")
