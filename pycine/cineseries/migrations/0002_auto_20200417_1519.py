# Generated by Django 3.0.4 on 2020-04-17 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cineseries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification_CSA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_CSA', models.CharField(max_length=20, verbose_name='Classification CSA')),
            ],
            options={
                'verbose_name': 'Classification CSA',
                'ordering': ['libelle_CSA'],
            },
        ),
        migrations.CreateModel(
            name='Realisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='Titre du film')),
            ],
            options={
                'verbose_name': 'Réalisateur',
                'ordering': ['nom'],
            },
        ),
        migrations.RemoveField(
            model_name='film',
            name='resume',
        ),
        migrations.AddField(
            model_name='film',
            name='date_sortie',
            field=models.DateTimeField(null=True, verbose_name='Date de sortie'),
        ),
        migrations.AddField(
            model_name='film',
            name='duree_film',
            field=models.TimeField(null=True, verbose_name='Durée'),
        ),
        migrations.AddField(
            model_name='film',
            name='synopsis',
            field=models.TextField(null=True, verbose_name='Synopsis'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='adresse',
            field=models.CharField(max_length=100, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='code_postal',
            field=models.CharField(max_length=5, null=True, verbose_name='Code postal'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='fermeture_exceptionnelle',
            field=models.CharField(max_length=100, null=True, verbose_name='Fermeture Exceptionnelle'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='nb_salles',
            field=models.IntegerField(null=True, verbose_name='Nombre de salles'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='ville',
            field=models.CharField(max_length=20, null=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='film',
            name='affiche',
            field=models.FileField(null=True, upload_to='', verbose_name='Affiche'),
        ),
        migrations.AlterField(
            model_name='film',
            name='titre',
            field=models.CharField(max_length=100, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='film',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cineseries.Classification_CSA'),
        ),
    ]
