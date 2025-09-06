from datetime import date


def date_formatter(country_code):
    formats = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }
    date_format = formats[country_code]

    def formatter(date):
        return date.strftime(date_format)
    return formatter

date_ru = date_formatter('ca')
today = date(2022, 1, 25)
print(date_ru(today))