from django import template
#from tickets.models import *

register = template.Library()

@register.simple_tag()
def get_menu():
    menu = [{"title": "Главная", "url_name": "home"},
            {"title": "Инфо", "url_name": "info"},
            {"title": "Рейсы", "url_name": "allFlyes"},
            {"title": "Список проданых билетов", "url_name": "soldTickets"},
            {"title": "Поиск рейса", "url_name": "flyght_search"},
            {"title": "Добавить рейс", "url_name": "add_flyght"},
            {"title": "Профиль", "url_name": "profile"},
            {"title": "расчет прибыли за день", "url_name": "day_profit"}
            #{"title": "Логин", "url_name": "log_in"},
            #{"title": "Регистрация", "url_name": "sign_in"}
            ]
    return menu