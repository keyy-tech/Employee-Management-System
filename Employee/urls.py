from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.custom_login_view, name="login"),
    path("logout/", views.custom_logout_view, name="logout"),
    path("create/", views.create_view, name="employee_create"),
    path("read/", views.read_view, name="employee_list"),
    re_path(
        r"^profile/(?P<employee_id>[a-zA-Z0-9]+)/$",
        views.profile_view,
        name="employee_profile",
    ),
    re_path(
        r"^update/(?P<employee_id>[a-zA-Z0-9]+)/$",
        views.update_view,
        name="employee_update",
    ),
    re_path(
        r"^delete/(?P<employee_id>[a-zA-Z0-9]+)/$",
        views.delete_view,
        name="employee_delete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
