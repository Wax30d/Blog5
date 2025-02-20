from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import homepage, post, about, search, postlist, allposts
from .views import AuthorViewSet, CategoryViewSet, PostViewSet, SignupView, LoginView, LogoutConfirmationView



router = DefaultRouter()

router.register(r'Authors', AuthorViewSet)

router.register(r'Categories', CategoryViewSet)

router.register(r'Posts', PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('post/<slug>/', post, name='post'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
    path('postlist/<slug>/', postlist, name='postlist'),
    path('posts/', allposts, name='allposts'),

    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutConfirmationView.as_view(), name='logout'),

]
