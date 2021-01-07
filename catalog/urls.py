from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book'),
    path('about/', views.about, name='about'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),  # views path for author_detail
    # tells us to go to the AuthorDetail class. ** GO TO VIEW **
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('staff/', views.StaffMemberListView.as_view(), name='staff_member'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('allborrowed/', views.all_borrowed, name='all-borrowed'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
