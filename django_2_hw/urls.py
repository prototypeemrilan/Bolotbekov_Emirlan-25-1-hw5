from django.contrib import admin
from django.urls import path
from products.views import main_page_view, products_view,hashtag_view, product_detail_view
from django.conf.urls.static import static
from django_2_hw.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('hashtag/', hashtag_view)
]

urlpatterns += static(MEDIA_URL, dociment_root=MEDIA_ROOT)