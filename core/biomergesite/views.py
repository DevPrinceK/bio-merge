from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'biomerge/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class UpdateDBSelectionView(View):
    template_name = 'biomerge/db_update_selection.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class LoadDataView(View):
    template_name1 = 'biomerge/db_update_selection.html'
    template_name1 = 'biomerge/db_update_selection.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)