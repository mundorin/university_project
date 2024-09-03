from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Flyes, SoldTickets, UserProfile
from .forms import SearchFlyForm, AddFlyghtForm, RegisterUserForm, LoginUserForm
from datetime import date


# Create your views here.

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "tickets/registration.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        profile = UserProfile(user=user, balance=0)
        profile.save()
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "tickets/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Логин"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class FlyesView(ListView):
    model = Flyes
    template_name = "tickets/allFlyes.html"
    context_object_name = "tickets"
    allow_empty = False#можно лит чтоб набор был пуст

    def get_context_data(self, *, objectlist=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список всех рейсов"
        return context

    def get_queryset(self):
        #id_num = self.kwargs['flightid']
        return Flyes.objects.filter(pk__gte=0)


class SoldTicketsView(ListView):
    model = SoldTickets
    template_name = "tickets/soldTickets.html"
    context_object_name = "tickets"

    def get_context_data(self, *, objectlist=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Список проданых билетов"
        return context

class FlightView(DetailView):
    model = Flyes
    template_name = "tickets/flight.html"
    context_object_name = "flight"
    #slug_url_kwarg = "flightid"
    pk_url_kwarg = "flightid"

    def get_context_data(self, *, objectlist=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Информация о билете"
        return context

def index(request):
    tickets = Flyes.objects.all()
    context = {
        "content": "This is ciontent",
        "tickets": tickets
    }
    return render(request, "tickets/index.html", context)

def soldTickets(request):
    tickets = SoldTickets.objects.all()
    context = {
        "title": "Список всех проданных билетов",
        "header": "Список всех проданных билетов",
        "tickets": tickets
    }
    return render(request, "tickets/soldTickets.html", context)

def allFlyes(request):
    tickets = Flyes.objects.all()
    context = {
        "content": "This is ciontent",
        "header": "Список всех рейсов",
        "tickets": tickets
    }
    return render(request, "tickets/allFlyes.html", context)

def info(request):
    return render(request, "tickets/info.html", {
        "content" : "This is content",
    })

def flyght_search(request):
    kw = {}
    search_results = []
    if request.method == 'POST':
        form = SearchFlyForm(request.POST)
        search_results = Flyes.objects.all()
        if form.is_valid():
            for i in form.cleaned_data:
                if request.POST[i]:
                    kw[i] = request.POST[i]
            search_results = search_results.filter(**kw)
            for i in search_results:
                print(i)
    else:
        form = SearchFlyForm()



    context = {
        "title": "Рейс",
        "flight": flight,
        "form": form,
        "search_results": search_results
    }
    return render(request, "tickets/search_flyght.html", context)

def flight(request, flightid):
    flight = Flyes.objects.get(pk=flightid)
    context = {
        "title": "Рейс",
        "flight": flight
    }
    return render(request, "tickets/flight.html", context)

def buy_tickets(request, flight_id):
    flight0 = Flyes.objects.get(id=flight_id)
    try:
        last_place = SoldTickets.objects.filter(flyes_id_id=flight_id).order_by('-place_number')[0].place_number
    except:
        last_place = 0
    b = SoldTickets(flyes_id=flight0, user=request.user, place_number=last_place+1)
    b.save()
    profile = get_object_or_404(UserProfile, user=request.user)
    #profile = UserProfile.objects.get(user=request.user)
    profile.bought_tickets.add(b)

    #flight = Flyes.objects.get(pk=flightid)
    context = {
        "title": "Рейс",
        "flight": flight
    }
    return render(request, "tickets/index.html", context)


def calculate_day_profit(request):

    todays_sold_tickets = SoldTickets.objects.filter(sold_date=date.today())
    sum = 0
    for i in todays_sold_tickets:
        sum += i.flyes_id.price
    print(sum)

    context = {
        "title": "Профиль",
        "profile": profile,
    }
    return render(request, "tickets/index.html", context)

def profile(request):
    context = {
        "title": "Профиль",
    }

    if request.user.is_authenticated:
        print("Пользователь авторизован")
        profile = get_object_or_404(UserProfile, user=request.user)
        bought_tickets = profile.bought_tickets.all()
        for i in bought_tickets:
            print(i.flyes_id_id)
        context['profile'] = profile
        context['bought_tickets'] = bought_tickets
    else:
        context['errors'] = ""
        print("Пользователь не авторизован")
        return redirect('login')

    return render(request, "tickets/profile.html", context)




def add_flyght(request):
    if request.method == 'POST':
        form = AddFlyghtForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SearchFlyForm()

    context = {
        "title": "Рейс",
        "flight": flight,
        "form": form,
    }
    return render(request, "tickets/add_flyght.html", context)

def logout_user(request):
    logout(request)
    return redirect('login')

def lal(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def registration(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def login(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')