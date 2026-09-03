from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, StudentProfile
from .forms import StudentForm, StudentProfileForm, StudentSearchForm


def student_list(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students}
    return render(request, 'core/student_list.html', context)


def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    # Profile exist garcha ki chaina check
    try:
        profile = student.profile
    except StudentProfile.DoesNotExist:
        profile = None
    context = {'student': student, 'profile': profile}
    return render(request, 'core/student_detail.html', context)


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student successfully added!")
            return redirect('student_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'core/student_create.html', context)


def student_update(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"{student.full_name} successfully updated!")
            return redirect('student_detail', slug=form.instance.slug)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = StudentForm(instance=student)
    context = {'form': form, 'student': student}
    return render(request, 'core/student_update.html', context)


def student_delete(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if request.method == 'POST':
        name = student.full_name
        student.delete()
        messages.success(request, f"{name} successfully deleted!")
        return redirect('student_list')
    context = {'student': student}
    return render(request, 'core/student_delete.html', context)


def student_search(request):
    form = StudentSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        name = form.cleaned_data.get('name')
        grade = form.cleaned_data.get('grade')
        gender = form.cleaned_data.get('gender')
        results = Student.objects.all()
        if name:
            results = results.filter(full_name__icontains=name)
        if grade:
            results = results.filter(grade=grade)
        if gender:
            results = results.filter(gender=gender)
    context = {'form': form, 'results': results}
    return render(request, 'core/student_search.html', context)


# PROFILE — create ya update
def student_profile(request, slug):
    student = get_object_or_404(Student, slug=slug)

    # Profile already cha bhane update, chaina bhane create
    try:
        profile = student.profile
    except StudentProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile:
            form = StudentProfileForm(request.POST, instance=profile)
        else:
            form = StudentProfileForm(request.POST)

        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.student = student
            profile_obj.save()
            messages.success(request, "Profile successfully saved!")
            return redirect('student_detail', slug=slug)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        if profile:
            form = StudentProfileForm(instance=profile)
        else:
            form = StudentProfileForm()

    context = {'form': form, 'student': student}
    return render(request, 'core/student_profile.html', context)