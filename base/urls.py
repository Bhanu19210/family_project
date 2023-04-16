from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_page,name = 'login_page' ),
    path('logout/',views.logout_page,name = 'logout'),
    path('home/',views.homepage, name='homepage'),
    path('Gen1/<slug:slug>/' ,views.family, name ='family'),
    path('Gen1/Gen2/<slug:slug>/',views.bro, name = 'bro'),
    path('Gen1/Gen2/Gen3/<slug:slug>/',views.sis, name = 'sis'),
] 
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('',views.login_page,name = 'login_page' ),
#     path('logout/',views.logout_page,name = 'logout'),
#     path('home/',views.homepage, name='homepage'),
#     path('family/<slug:slug>/' ,views.family, name ='family'),
#     path('family/child/<str:pk>/',views.bro, name = 'bro'),
#     path('sis/<str:pk>/',views.sis, name = 'sis'),
# ] 