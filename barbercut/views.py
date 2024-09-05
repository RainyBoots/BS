from django.shortcuts import render, redirect
from .forms import VisitModelForm 
from .models import Master, Service, Visit
from django.http import JsonResponse
from django.views.generic import View, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


MENU = [
        {'title': 'Главная', 'url': '/', 'active': True},
        {'title': 'Мастера', 'url': '#masters', 'active': True},
        {'title': 'Услуги', 'url': '#services', 'active': True},
        {'title': 'Отзывы', 'url': '#reviews', 'active': True},
        {'title': 'Запись на стрижку', 'url': 'visit/add/', 'active': True},
    ]

def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}


class MainView(View):
    def get(self, request):
        menu = get_menu_context()
        form = VisitModelForm()
        masters = Master.objects.all()

        return render(request, "main.html", {"form": form, "masters": masters, **menu})

    def post(self, request):
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")
        if form.errors:
            return render(
                request,
                "main.html",
                {"form": form, "masters": Master.objects.all(), **get_menu_context()},
            )



class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        return context

class VisitCreateView(CreateView):
    template_name = "visit_form.html"
    model = Visit
    form_class = VisitModelForm
    success_url = reverse_lazy("thanks")

class VisitDetailView(DetailView):
    template_name = "visit_detail.html"
    model = Visit
    context_object_name = "visit"


class VisitUpdateView(UpdateView):
    template_name = "visit_form.html"
    model = Visit
    form_class = VisitModelForm 
    success_url = reverse_lazy("thanks")

class VisitDeleteView(DeleteView):
    template_name = "visit_confirm_delete.html"
    model = Visit
    success_url = reverse_lazy("thanks")


class ServicesByMasterView(View):
    def get(self, request, master_id):
        if master_id:
            services = Service.objects.filter(masters__id=master_id).distinct()
            services_list = list(services.values('id', 'name', 'price'))
            return JsonResponse({'services': services_list})
        return JsonResponse({'services': []})