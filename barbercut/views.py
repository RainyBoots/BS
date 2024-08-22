from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Master, Service
from django.http import JsonResponse
from django.views import View

def main(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = AppointmentForm()

    masters = Master.objects.all()
    return render(request, 'main.html', {'form': form, 'masters': masters})


def thanks(request):
    return render(request, 'thanks.html')


class ServiceFetchView(View):
    def get(self, request, *args, **kwargs):
        master_id = request.GET.get('master_id')
        if master_id:
            services = Service.objects.filter(masters__id=master_id).distinct()
            services_list = list(services.values('id', 'name', 'price'))
            return JsonResponse({'services': services_list})
        return JsonResponse({'services': []})