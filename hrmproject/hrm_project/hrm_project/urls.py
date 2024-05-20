from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('hrm_app.urls')),
    path('login_panel/', include('users.urls')),

]
