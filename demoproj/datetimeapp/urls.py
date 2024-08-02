from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.current_datetime, name='current_datetime'),
    path('homes/',views.homes, name='homes'),
    path('userreg/',views.userreg, name='userreg'),
    path('insertuser/',views.insertuser, name='insertuser'),
]

urlpatterns += staticfiles_urlpatterns()
