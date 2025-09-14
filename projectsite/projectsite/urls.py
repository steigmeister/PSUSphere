from django.contrib import admin
from django.urls import path
## List Views
from studentorg.views import (
    HomePageView,
    OrganizationList,
    OrgMemberList,
    StudentList,
    CollegeList,
    ProgramList
)
## Create Views
from studentorg.views import (
    OrganizationCreateView,
    OrgMemberCreateView,
    StudentCreateView,
    CollegeCreateView,
    ProgramCreateView,
)
## Update Views
from studentorg.views import (
    OrganizationUpdateView,
    OrgMemberUpdateView,
    StudentUpdateView,
    CollegeUpdateView,
    ProgramUpdateView,
)
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),

    ## ListViews
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('orgmember_list', OrgMemberList.as_view(), name='orgmember-list'),
    path('student_list', StudentList.as_view(), name='student-list'),
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('program_list', ProgramList.as_view(), name='program-list'),

    ## CreateViews
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('orgmember_list/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    
    ## UpdateViews
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('orgmember_list/<pk>', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('college_list/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('program_list/<pk>', ProgramUpdateView.as_view(), name='program-update'),
]
