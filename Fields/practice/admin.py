from django.contrib import admin


from .models import Person, Team, PersonTeam, Friends, Message

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(PersonTeam)

admin.site.register(Friends)
admin.site.register(Message)