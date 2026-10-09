from django.contrib import admin
from django.urls import path, include
# from main import views


urlpatterns = [
    # path("", views.my_view, name="index"),
    # path("registrations/", views.register, name="register"),
    # path('registration/', views.register, name='register'),

    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),

]
