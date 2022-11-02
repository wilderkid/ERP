from django.urls import path
from . import views

app_name = 'cussystem'
urlpatterns = [
	path('index/', views.IndexView.as_view(), name='index'),
    path('orders/',views.OrdersView.as_view(), name='orders'),
	path('quotations/',views.QuotationsView.as_view(), name='quotations'),
	path('addwc/', views.addwc, name='addwc'),
	path('deleteswc/', views.deleteswc, name='deleteswc'),
	path('maincus/',views.MaincView.as_view(),name='maincus'),
	path('editwc/',views.editwc, name='editwc'),
	path('addtomainc/', views.addtomainc, name='addtomainc'),
	path('deletemcs/', views.deletemcs, name='deletemcs'),
	path('addquote/',views.addquote, name='addquote'),
	path("get_quotes/", views.get_quotes, name="get_quotes"),


	
]