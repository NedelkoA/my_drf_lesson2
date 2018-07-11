from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'categories', views.CategoryListView)
router.register(r'post', views.PostListView)

urlpatterns = [
    url(r'posts/api/', include(router.urls)),
    url(r'posts/api/users/$', views.UserListView.as_view()),
]
