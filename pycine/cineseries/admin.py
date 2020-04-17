from django.contrib import admin
from cineseries.models import Classification, Genre, Version, Cinema, Ouverture, Film, SeancesFilm, Serie, Saison, Episode, Acteur, Realisateur, UserProfileInfo, User

admin.site.register(Classification)
admin.site.register(Genre)
admin.site.register(Version)
admin.site.register(Cinema)
admin.site.register(Ouverture)
admin.site.register(Film)
admin.site.register(SeancesFilm)
admin.site.register(Serie)
admin.site.register(Saison)
admin.site.register(Episode)
admin.site.register(Acteur)
admin.site.register(Realisateur)
admin.site.register(UserProfileInfo)