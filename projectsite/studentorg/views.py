from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponse

## ListViews Here
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()

        today = timezone.now() .date()
        count = (
            OrgMember.objects.filter(
                date_joined__year=today.year
            )
            .values("student")
            .distinct()
            .count()
        )

        context["students_joined_this_year"] = count
        context["latest_organizations"] = count
        context["latest_programs"] = count
        return context       


class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
    ordering = ["college__college_name","name"]

    def get_queryset (self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5
    ordering = ["date_joined", "student__lastname"]

    def get_queryset (self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(student__icontains=query) |
                Q(organization__icontains=query) |
                Q(date_joined__icontains=query)
            )
        return qs
    def get_ordering(self):
        allowed = ["date_joined", "student__lastname"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "date_joined"

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

## CreateViews Here
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

## UpdateViews Here

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy ('organization-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy ('orgmember-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy ('student-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy ('college-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy ('program-list')

## DeleteView Here

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')





