from django.shortcuts import render, redirect
from apps.proveedores.models import Proveedor
from django.shortcuts import render,get_object_or_404
from .forms import ProvForm
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect

from django.views import View
def mostrarLogin(request):
    return render(request,'login.html')

def mostrarInicio(request):
    return render(request,'inicio.html')


class CtrlEditarProveedor(View):  
    @classmethod
    def mostrarProveedores(cls,request):
        LTP = Proveedor.objects.all()
        context = {
            'proveedores': LTP
        }
        return render(request,'proveedores.html',context)

    @classmethod
    def mostrarForm(cls,request, id):
        instance = get_object_or_404(Proveedor, id=id)
        form = ProvForm(instance=instance)
        return HttpResponse(form)

    @classmethod
    def guardarForm(cls,request,id):
        instance = get_object_or_404(Proveedor, id=id)
        if request.method == "POST":

            form = ProvForm(request.POST, instance=instance)
            
            if form.is_valid():
                form.save(commit=True)
        return HttpResponseRedirect('/proveedores')