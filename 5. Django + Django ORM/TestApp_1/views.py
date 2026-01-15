from datetime import date, time
from itertools import count

from django.db.models import Count, F, Q, Avg
from django.db.models.fields import return_None
from django.views.generic import ListView
from TestApp_1.models import *

class BookListView(ListView):

    model = Book
    context_object_name = 'books'
    template_name = 'Books_List.html'
    paginate_by = 20

    def get_queryset(self):
        # return Book.objects.filter(price__lt=500)
        # return Book.objects.filter(price__lte=300)
        # return Book.objects.filter(price__gt=1000)
        # return Book.objects.filter(price__gte=750)
        # return Book.objects.filter(title__icontains='Django')
        # return Book.objects.filter(title__icontains='python')
        # return Book.objects.filter(title__startswith='Advanced')
        # return Book.objects.filter(title__istartswith='pro')
        # return Book.objects.filter(title__endswith='Guide')
        # return Book.objects.filter(title__iendswith='tutorial')
        # return Book.objects.filter(published_date__year=2026)
        # return Book.objects.filter(title__regex=r"^Python")
        # return Book.objects.filter(published_date__year=2026)
        # return Book.objects.filter(published_date__month=1)
        # return Book.objects.filter(author__email='Vasenin@mail.ru')
        # return Book.objects.filter(author__last_name__icontains='Tolstoy')
        # return Book.objects.filter(metadata__genre='fiction')
        # return Book.objects.filter(metadata__tags__icontains='bestseller')
        # return Book.objects.filter(price=F('discount'))
        # return Book.objects.filter(price__gt=F('discount'))
        # return Book.objects.annotate(avg_rating=Avg('reviews__rating'))
        # return Book.objects.annotate(final_price=F('price') - F('discount'))
        return Book.objects.select_related('author')

class AuthorListView(ListView):

    model = Author
    context_object_name = 'authors'
    template_name = 'Authors_List.html'
    paginate_by = 20

    def get_queryset(self):
        # return Author.objects.filter(first_name = 'John')
        # return Author.objects.exclude(last_name='Doe')
        # return Author.objects.filter(id__in=[1,3,5]
        # return Author.objects.filter(last_name__iregex=r'^Mc')
        # return Author.objects.annotate(book_count=Count('books')).filter(book_count__gte=2)
        # return Author.objects.filter(Q(first_name='Aleksey') & ~Q(last_name='McVasenin'))
        # return Author.objects.annotate(count=Count('books'))
        return Author.objects.prefetch_related('books')

class ReviewListView(ListView):

    model = Review
    context_object_name = 'reviews'
    template_name = 'Reviews_List.html'
    paginate_by = 20

    def get_queryset(self):
        # return Review.objects.filter(comment='')
        # return Review.objects.exclude(comment='')
        # return Review.objects.filter(created_at__day=14)
        # return Review.objects.filter(created_at__week_day=3)
        # return Review.objects.filter(created_at__date=date(2026, 1, 14))
        # return Review.objects.filter(created_at__time=time(15, 30))
        # return Review.objects.filter(created_at__hour=15)
        # return Review.objects.filter(created_at__minute=30)
        return Review.objects.filter(created_at__second=00)
