from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path( 'register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name = 'users/login.html') ,name='login'),
    path('logout/', authentication_views.LogoutView.as_view(next_page=reverse_lazy('logout_success')), name='logout'),
    path('success/', authentication_views.TemplateView.as_view(template_name='users/logout.html'), name='success'),
    path('profile', user_views.profilepage, name='profile'),
    
]   

urlpatterns += [

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
