from django.urls import path, include
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
    path('products/search/', views.search),
    path('products/<str:category_slug>/<str:product_slug>/', views.ProductDetial.as_view()),
    path('products/<str:category_slug>/', views.CategoryDetail.as_view()),
]
