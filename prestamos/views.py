from django.shortcuts import render,redirect
from .models import Prestamo
from .forms import PrestamoForm
# Create your views here.


def ListarPrestamos(request):
    #ORM Captura todos los gatos de la BBDD -> all() -> select * from Gato
    prestamos = Prestamo.objects.all()
    return render(request, 'paginaBootstrap-5.html',{'prestamos':prestamos})

def NuevoPrestamo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo= form.save(commit=False)
            form.save()
        return redirect(to="ListarPrestamos")
    else:
        form = PrestamoForm()
        return render(request,'agregarPrestamo.html',{'form':form})

def FiltroPorID(request):
    prestamos = Prestamo.objects.filter(prestamoid=request.POST['filtrar'])
    return render(request, 'paginaBootstrap-5.html',{'prestamos':prestamos})

def EliminarPrestamo(request, id):
    prestamo = Prestamo.objects.get(prestamoid=id)
    prestamo.delete()
    return redirect(to="ListarPrestamos")

def ModificarPrestamo(request,id):
    prestamo = Prestamo.objects.get(prestamoid=id)
    datos = {
        'form':PrestamoForm(instance=prestamo)
    }
    if request.method=="POST":
        form= PrestamoForm(data=request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
        return redirect(to="ListarPrestamos")
    return render(request, 'modificarPrestamo.html',datos)