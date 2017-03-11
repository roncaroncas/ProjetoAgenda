from django.shortcuts import render, reverse

# Create your views here.

def index(request):
	return render(request, 'agenda/index.html')

#VIEWS RELACIONADOS A UM USUARIO
def profile(request):
	return render(request, 'agenda/profile.html')

def friends(request):
	return render(request, 'agenda/friends.html')

def groups(request):
	return render(request, 'agenda/groups.html')

def calendar(request):
	return render(request, 'agenda/calendar.html')

#VIEWS RELACIONADAS A UM GRUPO
#group
#members
#calendar
#...

