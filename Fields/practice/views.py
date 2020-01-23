from django.shortcuts import render
from .models import Person, Team, PersonTeam, Friends, Message


def manytomany(request):
    persons = Person.objects.all()
    teams = Team.objects.all()
    lists = PersonTeam.objects.all()
    context = {
        'persons': persons,
        'teams': teams,
        'lists': lists,
    }
    return render(request, 'practice/manytomany.html' ,context)

def onetomany(request):
    friends = Friends.objects.all()
    messages = Message.objects.all()
    context = {
        'friends': friends,
        'messages': messages,
    }
    return render(request, 'practice/onetomany.html', context)