from django.core.exceptions import BadRequest
from django.http import HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render
from .forms import HotelForm
def index(request):
    # t = render_to_string('Ambrella/index.html')
    # return HttpResponse(t) // Пример ниже !!!!  можно так как 1 пример, можно как ниже!
    data = {
            'value': 1,
            'int': 2023,
            'bool': True,
            'float': 28.56,
            'get':(request.GET),
            }

    return render(request,'Ambrella/index.html',context=data)

Hotel = [
    {'id' : 1,  'FI' : 'Люкс', "Clas" : 'S', 'TV' : True, 'Booked': True, 'image_': '1.jpg'},
    {'id' : 2,  'FI' : 'Люкс №2', "Clas" : 'S', 'TV' : True,  'Booked': True, 'image_': '2.jpg'},
    {'id' : 3,  'FI' : 'Люкс №3', "Clas" : 'S', 'TV' : True,  'Booked': False, 'image_': '3.jpg'},
    {'id' : 4,  'FI' : 'Люкс №4', "Clas" : 'S', 'TV' : True,   'Booked': True, 'image_': '4.jpg'},
    {'id' : 5,  'FI' : 'Люкс №5', "Clas" : 'S', 'TV' : True,  'Booked': False, 'image_': '5.jpg'},
    {'id' : 6,  'FI' : 'Люкс №6', "Clas" : 'S', 'TV' : True,  'Booked': False, 'image_': '6.jpg'},
    {'id' : 7,  'FI' : 'Двух местная комната', "Clas" : 'A', 'TV' : False,  'Booked': True, 'image_': '7.jpg'},
    {'id' : 8,  'FI' : 'Двух местная комната', "Clas" : 'A', 'TV' : True,  'Booked': False, 'image_': '8.jpg'},
    {'id' : 9,  'FI' : 'Двух местная комната', "Clas" : 'A', 'TV' : True, 'Booked': True, 'image_': '9.jpg'},
    {'id' : 10, 'FI': 'Двух местная комната', "Clas" : 'B', 'TV' : False, 'Booked': False, 'image_': '10.jpg'},
    {'id' : 11, 'FI': 'Двух местная комната', "Clas" : 'B', 'TV' : False, 'Booked': True, 'image_': '11.jpg'},
    {'id' : 12, 'FI': 'Двух местная комната', "Clas" : 'B', 'TV' : True, 'Booked': False, 'image_': '12.jpg'}]


menu = [
    {'title': 'Главная страница', 'url_n': 'home'},
    {'title': 'О сайте', 'url_n': 'about'},
    {'title': 'Номера', 'url_n': 'surn'},
]

data = {'students': Hotel, 'menu': menu, 'student_url': 'students_id',}
def index(request):
    return render(request, 'women/index.html', context=data)
def about(request):
    return render(request, 'women/about.html', context=data)

def hotel(request):
    hostel: Hotel.objects.Booked()
    return(render, 'women/current_student.html')

def student_index(request, student_id):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HotelForm()

    if 1 <= student_id <= 13:
        current = Hotel[student_id - 1]
    data = {
        'form': form,
        'current': current
    }
    return render(request, 'women/current_student.html', data)

def Students_mainpage(request):
    return render(request, 'women/sername.html', context=data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def Forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>')
def InternalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>')
def ErrBadRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неверный запрос</h1>')
def err_400(request):
    raise BadRequest
def err_500(request):
    raise ffff
# имитация ошибки сервера