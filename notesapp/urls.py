from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'note', views.NoteViewSet, basename='note')
# urlpatterns = router.urls

urlpatterns = [
    # path('viewset/',include(router.urls)),
    path('note/',views.NoteListView.as_view(),name="listview"),
    path('note/<int:pk>/',views.NoteEdit.as_view(),name="listedit"),
    path('login/',views.Login.as_view(),name="login"),
    path('register/',views.RegisterApi.as_view(),name="register"),
    path('logout/',views.Logout.as_view(),name="logout")
]