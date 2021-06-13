# dprojx/urls.py
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from iapapp import views, ajaxviews
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

admin.site.site_header = "CMMS Administration"
admin.site.site_title = "CMMS Admin Portal"
admin.site.index_title = "Welcome to CMMS Development Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # url(r'^$',views.index,name='index'),
    # url(r'^iapapp/',include('iapapp.urls')),
    path('iap/', include('iapapp.urls')),
    # path('IAP/', include('iapapp.urls')),
    path('budget/', include('budget.urls')),
    url(r'^iapapp/user_login/$',views.user_login,name='user_login'),
    path('ajax/swal/', ajaxviews.test_view, name='field_reg'), 
    path('inline/', views.inline, name='inline'), 

    # path('ajax/parse-eqp-excel/', ajaxviews.ParseEqpExcel.as_view()),
    path('ajax/parse-eqp-excel/', ajaxviews.ParseEqpExcel),
    path('ajax/Eqpupload_/', ajaxviews.Eqpupload),
    path('iap/eqpupload/', ajaxviews.eqpuploaadform1),


    # url(r'^special/',views.special,name='special'),
    # url(r'^logout/$', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]