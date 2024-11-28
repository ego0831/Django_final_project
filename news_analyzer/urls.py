
from django.urls import path
from django.contrib.auth import views as auth_views  # auth_views 임포트 추가
from . import views

urlpatterns = [
    # 홈 페이지 URL
    path('', views.index_view, name='index'),

    # 로그인 및 로그아웃 URL 설정
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    # 마이페이지
    path('mypage/', views.mypage_view, name='mypage'),

    # MBTI 기능 URL 설정
    path('mbti_test/', views.mbti_test, name='mbti_test'),
    path('mbti_result/', views.mbti_result, name='mbti_result'),

    # 관심 주식
    path('mystock/', views.mystock, name='mystock'),

    # News 경로
    path('News_home/', views.News_home, name='News_home'),
    path('News_lastest/', views.News_lastest, name='News_lastest'),
    path('hot_topic/', views.hot_topic, name='hot_topic'),

    # 주식 추천
    path('stock_recommendations/', views.stock_recommendations, name='stock_recommendations'),




]