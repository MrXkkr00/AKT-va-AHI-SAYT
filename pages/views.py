from django.shortcuts import render
from django.views import View


# Create your views here.


class HomePagesViews(View):
    def get(self, requset):
        return render(requset, "index.html")


class AboutPagesViews(View):
    def get(self, requset):
        return render(requset, "about.html")


class BlogPagesViews(View):
    def get(self, requset):
        return render(requset, "blog.html")


class BlogSinglePagesViews(View):
    def get(self, requset):
        return render(requset, "blog-single.html")

class ContactPagesViews(View):
    def get(self, requset):
        return render(requset, "contact.html")


class CoursesSinglePagesViews(View):
        def get(self, requset):
            return render(requset, "course-single.html")


class CoursesPagesViews(View):
    def get(self, requset):
        return render(requset, "courses.html")



class EventSinglePagesViews(View):
    def get(self, requset):
        return render(requset, "event-single.html")


class EventsPagesViews(View):
    def get(self, requset):
        return render(requset, "events.html")


class NoticePagesViews(View):
    def get(self, requset):
        return render(requset, "notice.html")



class NoticeSinglePagesViews(View):
    def get(self, requset):
        return render(requset, "notice-single.html")



class ResearchPagesViews(View):
    def get(self, requset):
        return render(requset, "research.html")

class ScholarshipPagesViews(View):
        def get(self, requset):
            return render(requset, "scholarship.html")



class TeacherPagesViews(View):
    def get(self, requset):
        return render(requset, "teacher.html")



class TeacherSinglePagesViews(View):
    def get(self, requset):
        return render(requset, "teacher-single.html")