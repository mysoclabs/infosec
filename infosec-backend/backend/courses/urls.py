from django.urls import path
from .views import (
	course_list,
	course_detail,
	enroll,
	enrollment_status,
	lesson_progress,
	mark_lesson_complete,
)


urlpatterns = [
    path("", course_list, name="course-list"),
    path("<slug:slug>/", course_detail, name="course-detail"),
    path("<slug:slug>/enroll/", enroll, name="course-enroll"),
    path("<slug:slug>/enrollment/", enrollment_status, name="course-enrollment-status"),
    path("<slug:slug>/progress/", lesson_progress, name="course-lesson-progress"),
    path(
		"<slug:slug>/lessons/<str:lesson_id>/complete/",
		mark_lesson_complete,
		name="course-lesson-complete",
	),
]


