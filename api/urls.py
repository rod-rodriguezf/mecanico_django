from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    url(r'^api/repuestos/$', views.RepuestosViewSet.as_view()),
    url(r'^api/repuestos_crear/$', views.RepuestosCreateViewSet.as_view()),
    url(r'^api/repuestos/(?P<nombre>.+)/$', views.RepuestosBuscarViewSet.as_view()),
]

urlpatterns= format_suffix_patterns(urlpatterns)