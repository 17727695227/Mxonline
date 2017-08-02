#__coding:utf-8__*__
__author__ = 'admin'
__date__ = '2017/3/27 22:00'

import xadmin

from courses.models import Course
from courses.models import Lesson
from courses.models import Video
from courses.models import CourseResource


class CourseAdmin(object):
        list_display = ['name', 'desc', 'detail', 'degree','learn_time', 'students', 'fav_nums', 'image','click_nums','add_time']
        search_fields = ['name', 'desc', 'detail', 'degree','learn_time', 'students', 'fav_nums', 'image','click_nums']
        list_filter = ['name', 'desc', 'detail', 'degree','learn_time', 'students', 'fav_nums', 'image','click_nums','add_time']


class LessonAdmin(object):
        list_display = ['course', 'name', 'add_time']
        search_fields =  ['course', 'name']
        list_filter =  ['course', 'name', 'add_time']


class VideaAdmin(object):
        list_display = ['lesson', 'name', 'add_time']
        search_fields =['lesson', 'name']
        list_filter = ['lesson', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name','download', 'add_time']
    search_fields =  ['course', 'name','download']
    list_filter =  ['course', 'name','download', 'add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideaAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)