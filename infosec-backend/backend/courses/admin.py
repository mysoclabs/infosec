from django.contrib import admin
from .models import Course, Enrollment, LessonProgress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "is_published", "created_at")
    list_filter = ("level", "is_published")
    search_fields = ("title",)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "is_paid")
    list_filter = ("is_paid", "course")
    search_fields = ("user__email", "course__title")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "lesson_id", "completed_at")
    list_filter = ("course", "user")
    search_fields = ("user__email", "course__title", "lesson_id")
    ordering = ("-completed_at",)
