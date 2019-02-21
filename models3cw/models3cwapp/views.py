from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Car


# CREATES NEW BOOK
def newBook(request):
    newObject = Book(name="Sun Book", genre='fiction', publishDate='2001-12-03')
    newObject.save()
    return HttpResponse(newObject)


# SHOWS ALL BOOKS
def allBooks(request):
    allEntries = Book.objects.all()
    return HttpResponse(allEntries)


# BOOK FILTER BY SPECIFIC YEAR
def greaterThan(request):
    objectsGreaterThanJan1 = Book.objects.filter(publishDate__gt='2018-01-01')
    return HttpResponse(objectsGreaterThanJan1)


# CREATES NEW CAR
def newCar(request):
    newObj = Car(make="Acura", model='Legend', year='1991-05-07')
    newObj.save()
    return HttpResponse(newObj)


# SHOWS ALL CARS
def allCars(request):
    allEnt = Car.year.objects.all()
    return HttpResponse(allEnt)


# CAR FILTER BY SPECIFIC YEAR
def greaterThanYear(request):
    objectsGreaterThanYear = Car.objects.filter(year__gt='2010-01-01')
    return HttpResponse(objectsGreaterThanYear)
