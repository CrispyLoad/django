from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import Person


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "application/edit.html", {"person": person})

    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиeнт не найден</h2>")


# def index(request):
#     #cat = []
#     #return render(request, "application/home_page.html", context={"cat": cat})
#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             name = user_form.cleaned_data["name"]
#             return HttpResponse(f"<h2>Имя введено корректно - {name}</h2>")
#         else:
#             return HttpResponse("Ошибка ввода данных")
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {"form": userform})
#     # userform = UserForm(field_order=["age", "name"])
#     # return render(request, 'index.html', {"form": userform})
#
#
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
#
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")
#
#
# def to_about(request):
#     return HttpResponseRedirect("/about")
#
#
# def to_start(request):
#     return HttpResponsePermanentRedirect("/")
#
#
# def products(request, productid=1):
#     category = request.GET.get("cat", "")
#     output = f"<h2>Продукт №{productid}, категория: {category}</h2>"
#     return HttpResponse(output)


# def users(request):
#     user_id = request.GET.get("id", 1)
#     name = request.GET.get("name", "Максим")
#     output = f"<h2>Пользователь</h2><h3>id: {user_id} Имя:{name}</hЗ>"
#     return HttpResponse(output)
