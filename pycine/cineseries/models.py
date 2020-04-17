from django.db import models

class Classification(models.Model): # Classification CSA
    libelle = models.CharField(max_length=40, null=False, verbose_name='Classification')

    class Meta:
        verbose_name = "Classification"
        ordering = ['libelle']

    def __str__(self):
        return '{}'.format(self.libelle)

class Genre(models.Model): # Comédie, Thriller, Drame...
    libelle = models.CharField(max_length=30, null=False, verbose_name='Genre')

    class Meta:
        verbose_name = "Genre"
        ordering = ['libelle']

    def __str__(self):
        return '{}'.format(self.libelle)

class Version(models.Model): # VO, VF, VOSTFR...
    libelle = models.CharField(max_length=10, null=False, verbose_name='Version')

    class Meta:
        verbose_name = "Version"
        ordering = ['libelle']

    def __str__(self):
        return '{}'.format(self.libelle)

class Cinema(models.Model):
    nom = models.CharField(max_length=40, null=False, verbose_name='Nom')
    nb_salles = models.IntegerField(null=True, verbose_name='Nombre de salles')
    adresse = models.CharField(max_length=100, null=True, verbose_name='Adresse')
    #Attention faute dans le MCD Code postal : Int --> varchar
    code_postal = models.CharField(max_length=5, null=True, verbose_name='Code postal')
    ville = models.CharField(max_length=20, null=True, verbose_name='Ville')
    fermeture_exceptionnelle = models.TextField(max_length=100, null=True, verbose_name='Fermeture Exceptionnelle')
    
    class Meta:
        verbose_name = "Cinéma"
        ordering = ['nom']

    def __str__(self):
        return '{}'.format(self.nom)

class Ouverture(models.Model):
    jour = models.CharField(max_length=10, null=False, verbose_name='Jour de la semaine')
    heure_ouverture = models.TimeField(null=False, verbose_name='Heure d''ouverture')
    heure_fermeture = models.TimeField(null=False, verbose_name='Heure de fermeture')
    # Associations
    cinemas = models.ManyToManyField(Cinema, related_name='ouvertures_cinemas')

    class Meta:
        verbose_name = "Ouverture"
        ordering = ['jour']

    def __str__(self):
        return '{}'.format(self.jour)

class Film(models.Model):
    titre = models.CharField(max_length=100, null=False, verbose_name='Titre')
    synopsis = models.TextField(null=True, verbose_name='Synopsis')
    date_sortie = models.DateField(null=True, verbose_name='Date de sortie')
    affiche = models.FileField(null=True, verbose_name='Affiche')
    duree = models.TimeField(null=True, verbose_name='Durée')
    note_moyenne = models.IntegerField(null=True, verbose_name='Note moyenne')
    # Associations
    cinemas = models.ManyToManyField(Cinema, related_name='films_cinemas')
    classification = models.ForeignKey(Classification, null=True, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='films_genres')
 
    class Meta:
        verbose_name = 'Film'
        ordering = ['titre']
    
    def __str__(self):
        return '{}'.format(self.titre)
    
class SeancesFilm(models.Model):
    numero_salle = models.IntegerField(null=False, verbose_name='Numéro de salle')
    # Attention faute dans le MCD Date séance : date --> datetime
    date_seance = models.DateTimeField(null=False, verbose_name="Date et heure de la séance")
    # Associations
    film = models.ForeignKey(Film, null=False, on_delete=models.CASCADE, related_name='+')
    cinema = models.ForeignKey(Cinema, null=False, on_delete=models.CASCADE, related_name='+')
    version = models.ForeignKey(Version, null=True, on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Séances film"
        ordering = ['date_seance']

    def __str__(self):
        return '{}'.format(self.date_seance)

class Serie(models.Model):
    titre = models.CharField(max_length=100, null=False, verbose_name='Titre')
    synopsis = models.TextField(null=True, verbose_name='Synopsis')
    note_moyenne = models.IntegerField(null=True, verbose_name='Note moyenne')
    # Associations
    classification = models.ForeignKey(Classification, null=True, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='series_genres')
    versions = models.ManyToManyField(Version, related_name='series_versions')
    
    class Meta:
        verbose_name = 'Série'
        ordering = ['titre']
    
    def __str__(self):
        return '{}'.format(self.titre)
    
class Saison(models.Model):
    numero = models.CharField(max_length=100, null=False, verbose_name='Numéro')
    synopsis = models.TextField(null=True, verbose_name='Synopsis')
    affiche = models.FileField(null=True, verbose_name='Affiche')
    note_moyenne = models.IntegerField(null=True, verbose_name='Note moyenne')
    # Associations
    serie = models.ForeignKey(Serie, null=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Saison'
        ordering = ['numero']
    
    def __str__(self):
        return '{}'.format(self.numero)

class Episode(models.Model):
    titre = models.CharField(max_length=100, null=False, verbose_name='Titre')
    synopsis = models.TextField(null=True, verbose_name='Synopsis')
    date_sortie = models.DateField(null=True, verbose_name='Date de sortie')
    affiche = models.FileField(null=True, verbose_name='Affiche')
    duree = models.TimeField(null=True, verbose_name='Durée')
    note_moyenne = models.IntegerField(null=True, verbose_name='Note moyenne')
    # Associations
    saison = models.ForeignKey(Saison, null=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Episode'
        ordering = ['titre']
    
    def __str__(self):
        return '{}'.format(self.titre)

class Acteur(models.Model):
    nom = models.CharField(max_length=20, null=False, verbose_name='Nom')
    prenom = models.CharField(max_length=20, null=True, verbose_name='Prénom')
    sexe = models.CharField(max_length=1, null=True, verbose_name='Sexe')
    date_naissance = models.DateField(null=True, verbose_name='Date de naissance')
    biographie = models.TextField(null=True, verbose_name='Biographie')
    pays_naissance = models.CharField(max_length=20, null=True, verbose_name='Pays')
    # Associations
    films = models.ManyToManyField(Film, related_name='acteurs_films')
    episodes = models.ManyToManyField(Episode, related_name='acteurs_episodes')
    
    class Meta:
        verbose_name = 'Acteur'
        ordering = ['nom']
    def __str__(self):
        return '{}'.format(self.nom)

class Realisateur(models.Model):
    nom = models.CharField(max_length=20, null=False, verbose_name='Nom')
    prenom = models.CharField(max_length=20, null=True, verbose_name='Prénom')
    sexe = models.CharField(max_length=1, null=True, verbose_name='Sexe')
    date_naissance = models.DateField(null=True, verbose_name='Date de naissance')
    pays_naissance = models.CharField(max_length=20, null=True, verbose_name='Pays')
    biographie = models.TextField(null=True, verbose_name='Biographie')
    # Associations
    films = models.ManyToManyField(Film, related_name='realisateurs_films')
    episodes = models.ManyToManyField(Episode, related_name='realisateurs_episodes')
    
    class Meta:
        verbose_name = 'Réalisateur'
        ordering = ['nom']
    
    def __str__(self):
        return '{}'.format(self.nom)

from django.contrib.auth.models import User #Accès aux modèles Django de gestion des utilisateurs

class UserProfileInfo(models.Model): #Infos persos
    #On lie les infos persos aux infos de connexion gérées par Django à travers la classe User
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user_profile')
    avatar = models.FileField(upload_to='avatars',blank=True)
    films = models.ManyToManyField(Film, blank=True, related_name='user_films')
    cinemas = models.ManyToManyField(Cinema, blank=True, related_name='user_cinemas')

    class Meta:
        verbose_name = 'Utilisateur'
        ordering = ['user']
    
    def __str__(self):
        return self.user.username

class Critique(models.Model):
    note = models.IntegerField(null=False, verbose_name='Note attribuée')
    titre = models.CharField(max_length=100,null=False, verbose_name="Titre")
    message = models.TextField(null=False, verbose_name="Message")
    # Associations
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE, related_name='+')
    serie = models.ForeignKey(Serie, null=True, on_delete=models.CASCADE, related_name='+')
    saison = models.ForeignKey(Saison, null=True, on_delete=models.CASCADE, related_name='+')
    episode = models.ForeignKey(Episode, null=True, on_delete=models.CASCADE, related_name='+')
    
    class Meta:
        verbose_name = "Critique"
        ordering = ['user']

    def __str__(self):
        return '{}'.format(self.note)