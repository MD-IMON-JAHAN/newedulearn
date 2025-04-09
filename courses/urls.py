from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    # Web Views
    course_list, course_create, course_update, course_delete, course_detail,
    lesson_create, lesson_update, lesson_delete,
    enroll_student, view_students,
    register, user_login, user_logout, profile,
    
    # Class-Based Views
    CourseListView, CourseDetailView, CourseCreateView,
    
    # API Views
    CourseListAPI, CourseDetailAPI, EnrollStudentAPI
)

urlpatterns = [
    # Course Management URLs
    path('', course_list, name='course_list'),
    path('create/', course_create, name='course_create'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('<int:course_id>/update/', course_update, name='course_update'),
    path('<int:course_id>/delete/', course_delete, name='course_delete'),
    
    # Lesson Management URLs
    path('lesson/create/', lesson_create, name='lesson_create'),
    path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
    path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),
    
    # Student Management URLs
    path('enroll/', enroll_student, name='enroll_student'),
    path('course/<int:course_id>/students/', view_students, name='view_students'),
    
    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    
    # Password Management URLs
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='courses/password_change.html'), 
         name='password_change'),
    path('password_change_done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='courses/password_change_done.html'), 
         name='password_change_done'),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html'), 
         name='password_reset'),
    path('password_reset_done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'), 
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='courses/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password_reset_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='courses/password_reset_complete.html'), 
         name='password_reset_complete'),
    
    # API Endpoints
    path('api/courses/', CourseListAPI.as_view(), name='api_course_list'),
    path('api/courses/<int:pk>/', CourseDetailAPI.as_view(), name='api_course_detail'),
    path('api/enroll/', EnrollStudentAPI.as_view(), name='api_enroll_student'),
]