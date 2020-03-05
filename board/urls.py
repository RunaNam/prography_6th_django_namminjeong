from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from board import views

app_name = 'board'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.PostViewSet.as_view(), name='board_list'),
    path('board/', views.PostViewSet.as_view(), name='board_list'),
    path('board/create/', views.PostCreateViewSet.as_view(), name='board_create'),
    path('board/<int:pk>/', views.PostDetailViewSet.as_view(), name='board_detail'),
    path('board/<int:pk>/change/', views.PostUpdateDestroyAPIViewSet.as_view(), name='board_update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
