from django.urls import path
from . import views


urlpatterns = [
    path('loginapi',views.loginapi,name="loginapi"),
    path('registerapi',views.registerapi,name="registerapi"),
    path('logoutapi',views.logoutapi,name="logoutapi"),
    path('createnoteapi',views.createnoteapi,name="createnoteapi"),
    path('updatenoteapi',views.updatenoteapi,name="createnoteapi"),
    path('deletenoteapi',views.deletenoteapi,name="createnoteapi"),
    path('getnoteapi',views.getnoteapi,name='getnextnote')
    # path('myapi/',views.myloginapi,name='myapi'),

]