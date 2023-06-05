from django.urls import path
from .views import HomePagesViews,\
    TeacherPagesViews, TeacherSinglePagesViews,\
    CoursesSinglePagesViews, NoticeSinglePagesViews,\
    AboutPagesViews, BlogPagesViews,\
    ContactPagesViews, EventsPagesViews,\
    ResearchPagesViews, BlogSinglePagesViews,\
    EventSinglePagesViews, CoursesPagesViews,\
    NoticePagesViews, ScholarshipPagesViews


urlpatterns = [
    path('about', AboutPagesViews.as_view(), name='about'),
    path('blog', BlogPagesViews.as_view(), name='blog'),
    path('blog_single', BlogSinglePagesViews.as_view(), name='blog-single'),
    path('contact', ContactPagesViews.as_view(), name='contact'),
    path('course-single', CoursesSinglePagesViews.as_view(), name='course-single'),
    path('courses', CoursesPagesViews.as_view(), name='courses'),
    path('event-single', EventSinglePagesViews.as_view(), name='event-single'),
    path('events', EventsPagesViews.as_view(), name='events'),
    path('index', HomePagesViews.as_view(), name='index'),
    path('', HomePagesViews.as_view(), name='home'),
    path('notice', NoticePagesViews.as_view(), name='notice'),
    path('notice-single', NoticeSinglePagesViews.as_view(), name='notice-single'),
    path('research', ResearchPagesViews.as_view(), name='research'),
    path('scholarship', ScholarshipPagesViews.as_view(), name='scholarship'),
    path('teacher', TeacherPagesViews.as_view(), name='teacher'),
    path('teacher-single', TeacherSinglePagesViews.as_view(), name='teacher-single')

]