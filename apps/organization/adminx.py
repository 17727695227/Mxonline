#__coding:utf-8__*__
__author__ = 'admin'
__date__ = '2017/3/25 0:08'
import xadmin

from .models import CityDict
from .models import CourseOrg
from .models import Teacher

class CityDictAdmin(object):
    list_display=['name','desc','add_time']
    search_fields=['name','desc']
    list_filter=['name','desc','add_time']


class CourseOrgAdmin(object):
    list_display=['name','desc','click_nums','fav_nums','image','address','city','add_time']
    search_fields=['name','desc','click_nums','fav_nums','image','address','city']
    list_filter=['name','desc','click_nums','fav_nums','image','address','city','add_time']


class TeacherAdmin(object):
    list_display=['ord','name','work_years','work_compay','work_position','points','click_nums','fav_nums','add_time']
    search_fields=['ord','name','work_years','work_compay','work_position','points','click_nums','fav_nums']
    list_filter=['ord','name','work_years','work_compay','work_position','points','click_nums','fav_nums','add_time']



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
