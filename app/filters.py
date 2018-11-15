from django.contrib.admin.filters import AllValuesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = '../templates/dashboard.html'