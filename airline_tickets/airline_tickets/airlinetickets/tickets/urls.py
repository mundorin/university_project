from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info,  name='info'),
    path('sold_tickets/', SoldTicketsView.as_view(),  name='soldTickets'),
    path('flyes/', FlyesView.as_view(),  name='allFlyes'),
    path('flight/<int:flightid>/', FlightView.as_view(), name='flight'),
    path('flight_search/', flyght_search, name='flyght_search'),
    path('add_flyght/', add_flyght, name='add_flyght'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('buy/<int:flight_id>/', buy_tickets, name='buy_ticket'),
    path('day_profit/', calculate_day_profit, name='day_profit')
]