from django.shortcuts import render, redirect
from cartaoApp.forms import ValidarForm
from cartaoApp.models import  Validar
# Create your views here.
def ola(request):
    return render(request,'cartao/parabens.html')

def index(request):
    return  render(request,'cartao/index.html')

def consulta(request):
    form =ValidarForm(request.POST)
    if request.method == "POST":
        form=ValidarForm(request.POST, request.FILES)
        if form.is_valid():
            obj =form.save()
            obj.save()
            form=ValidarForm()
            return redirect('ola')
    return  render(request,'cartao/consulta.html',{'form':form})

def mostrar_dados(request):
    validados = Validar.objects.all()
    context = {"validados": validados}
    return render(request, "cartao/mostrar_dados.html", context)

def mostrar_cartao(request):
    validados = Validar.objects.all()
    context = {"validados": validados}
    return render(request, "cartao/mostrar_cartao.html", context)

