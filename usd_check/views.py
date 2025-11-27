from django.shortcuts import render
from django.http import JsonResponse
from .models import ExchangeRate
from django.utils import timezone
import requests
import datetime

# Create your views here.

def get_current_usd(request):
    """
    Обновляет курс USD к RUB (не чаще раза в 10 секунд) и возвращает
    текущее значение вместе с историей последних 10 записей.
    """
    target_currency = 'RUB'
    source = "Database"  # Источник данных по умолчанию
    server_time = timezone.now()

    # Проверяем: хочет ли клиент HTML (значит, это просто открытие страницы в браузере)
    is_html_request = 'text/html' in request.headers.get('Accept', '')

    # ВАЖНО: Заходим в блок обновления, ТОЛЬКО если это НЕ html-запрос
    # (то есть, если это JSON-запрос от кнопки)
    if not is_html_request:
        last_record = ExchangeRate.objects.filter(currency=target_currency).last()

        # Если запись есть и с момента ее создания прошло меньше 10 секунд
        if not last_record or (server_time - last_record.created_at) > datetime.timedelta(seconds=10):
            try:
                url = f"https://api.exchangerate-api.com/v4/latest/USD"
                response = requests.get(url)
                response.raise_for_status()  # Проверка на ошибки HTTP (4xx или 5xx)
                data = response.json()
                if data and 'rates' in data and target_currency in data['rates']:
                    rate_value = data['rates'][target_currency]
                    ExchangeRate.objects.create(currency=target_currency, rate=rate_value)
                    source = "ExchangeRate-API"  # Обновляем источник, если запрос успешен
            except requests.RequestException:
                # Если API недоступен, мы просто отдадим старые данные из БД.
                # Источник останется "Database".
                pass

    # --- Сбор данных для ответа ---

    # Получаем текущий (самый последний) курс из БД
    current_rate_obj = ExchangeRate.objects.filter(currency=target_currency).last()
    current_data = None
    if current_rate_obj:
        current_data = {
            'rate': current_rate_obj.rate,
            'date_iso': current_rate_obj.created_at.isoformat(),
            'date_formatted': current_rate_obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    # Получаем историю последних 10 записей
    history_qs = ExchangeRate.objects.filter(currency=target_currency).order_by('-created_at')[:10]
    history_data = []
    for item in history_qs:
        history_data.append({
            'rate': item.rate,
            'date_iso': item.created_at.isoformat(),
            'date_formatted': item.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    # Формируем финальный JSON-ответ
    response_data = {
        "meta": {
            "status": "success",
            "source": source,
            "server_time": server_time.isoformat()
        },
        "data": {
            "current": current_data,
            "history": history_data
        }
    }
    if 'text/html' in request.headers.get('Accept', ''):
        return render(request, 'index.html', { \
        'current': current_data,
        'history': history_data
        })
    return JsonResponse(response_data)