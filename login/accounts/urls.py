from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns=[
    #path('', include('django.contrib.auth.urls')),
    path('',views.dashboardView,name="index"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('viewimages/',views.viewImages,name="viewImages"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('map/',views.map,name="map"),
    #path('home/',home.as_view(next_page='dashboard'),name="home_url"),
    path('dashboard/home/',views.home,name="home_url"),
    path('dashboard/cluster/',views.cluster,name="cluster"),
    path('dashboard/home/<str:clusterid>',views.home,name="home_url_id"),
    path('dashboard/checkCluster/',views.updateOnCluster,name="cluster_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),

    path('password_reset',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset/complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
