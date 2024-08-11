import re
from datetime import date, timedelta, datetime


def string_to_date(date_string, date_format="%Y-%m-%d"):
    try:
        date_object = datetime.strptime(date_string, date_format).date()
        return date_object
    except ValueError:
        return None
def calculate_age(birthdate):
    birthdate = string_to_date(birthdate)
    today = date.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        last_month = (today.replace(day=1) - timedelta(days=1)).day
        days += last_month

    if months < 0:
        years -= 1
        months += 12

    return age_in_years(years, months, days)


def age_in_years(years, months, days):
    days_in_year = 365.25  # Average days in a year accounting for leap years
    days_in_month = days_in_year / 12

    total_days = years * days_in_year + months * days_in_month + days
    age_in_years = total_days / days_in_year

    return age_in_years


def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # If the string matches the regex, it is a valid email
    return re.match(email_regex, email) is not None


def is_digits_only(input_string):
    # Regular expression for digits only
    digits_regex = r'^[0-9]+$'

    return re.match(digits_regex, input_string) is not None
def registervalidation(values):
    message = []
    # if values['username'] == '':
    #     message.append({'username': 'username is require field'})
    if values['email'] == '':
        message.append({'email': 'email is require field'})
    elif not is_valid_email(values['email']):
        message.append({'email': 'email is invalid format'})
    if values['password1'] == '':
        message.append({'password1': 'password1 is require field'})
    elif len(values['password1']) < 8:
        message.append({'password1': 'password1 is at least 8 charactors.'})
    if values['password2'] == '':
        message.append({'password2': 'password2 is require field'})
    elif values['password1'] != values['password2']:
        message.append({'password2': 'password and confirm password is not match'})
    if values['firstname'] == '':
        message.append({'firstname': 'firstname is require field'})
    if values['lastname'] == '':
        message.append({'lastname': 'lastname is require field'})
    if values['address'] == '':
        message.append({'address': 'lastname is require field'})
    if values['birthday'] == '':
        message.append({'birthday': 'birthday is require field'})
    elif calculate_age(values['birthday']) < 18:
        message.append({'birthday': 'Cannot create for under age 18.'})
    if values['phone'] == '':
        message.append({'phone': 'phone is require field'})
    elif not is_digits_only(values['phone']):
        message.append({'phone': 'please input 0 to 9 only'})
    elif len(values['phone']) < 9 or len(values['phone']) > 11:
        message.append({'phone': 'please input at least 9 digits or maximum 12 digit'})
    return message