from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Store, Condition
from django.contrib.auth.decorators import login_required

from .forms import CourseForm


def all_courses(request):
    """ 
    A view to show all courses
    """
    store = Store.objects.all()
    context = {
        'store': store,
    }
    return render(request, 'store/store.html', context)


def course_detail(request, store_id):
    """
    A view to show selected course details
    """
    store = get_object_or_404(Store, pk=store_id)
    context = {
        'store': store,
    }
    return render(request, 'store/course_detail.html', context)


@login_required
def add_course(request):
    """
    Add a course to the store
    """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('store'))
    else:
        form = CourseForm()

    template = 'store/add_course.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_course(request, store_id):
    """
    Edit a course in the store
    """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    store = get_object_or_404(Store, pk=store_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            return redirect(reverse('store'))
    else:
        form = CourseForm(instance=store)

    template = 'store/edit_course.html'
    context = {
        'form': form,
        'store': store,
    }
    return render(request, template, context)


@login_required
def delete_course(request, store_id):
    """
    Delete a course from the store
    """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return redirect(reverse('store'))
