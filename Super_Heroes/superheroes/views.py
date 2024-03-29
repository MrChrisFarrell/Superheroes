from django.shortcuts import render
from .models import Superhero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')


def edit(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    if request.method == 'POST':
        hero.name = request.POST.get('name')
        hero.alter_ego = request.POST.get('alter_ego')
        hero.primary_ability = request.POST.get('primary_ability')
        hero.secondary_ability = request.POST.get('secondary_ability')
        hero.catch_phrase = request.POST.get('catch_phrase')
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
            'hero': hero
        }
        return render(request, 'superheroes/edit.html', context)


def delete(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    hero.delete()
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)


def detail(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheroes/detail.html', context)
