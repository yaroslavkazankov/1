from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'

    context = {'students': Student.objects.prefetch_related('teacher').order_by('group').all()}

    breakfast = Menu.objects.get(name='Breakfast')
    all_items_with_breakfast_menu = Item.objects.filter(menu=breakfast)
    same_all_items_with_breakfast_menu = breakfast.item_set.all()
    print(context)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
