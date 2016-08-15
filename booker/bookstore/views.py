from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from bookstore.models import Book, Category

class HomeView(TemplateView):
    template_name = "bookstore/index.html"


class ResultView(TemplateView):
    template_name = 'bookstore/result.html'


    def get(self, request, *args, **kwargs):


        book_or_category = request.GET.get('name')

        context = {}
        import pdb; pdb.set_trace()
        option = request.GET.get('bookerOptions')

        if option == 'book':
            books = Book.objects.filter(name__contains=book_or_category)


        elif option == 'category':
            categories = Category.objects.get(name=book_or_category)
            books = Book.objects.filter(category=categories)


        context = {'books': books}


        return render(request, 'bookstore/result.html', context)

