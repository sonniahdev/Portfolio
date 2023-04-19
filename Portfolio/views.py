from django.shortcuts import render, redirect


def indexpage(request):
    return render(request, 'index.html')