# Put you code here
from django import template

register = template.Library()
persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
english_numbers = '1234567890'

def persian_digit(text:str):
    for digit in range(10):
        text = text.replace(english_numbers[digit],persian_numbers[digit])
    return text


register.filter('persian_digit', persian_digit)
