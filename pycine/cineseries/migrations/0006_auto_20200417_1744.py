# Generated by Django 3.0.4 on 2020-04-17 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cineseries', '0005_userprofileinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20, verbose_name='Classification')),
            ],
            options={
                'verbose_name': 'Classification',
                'ordering': ['libelle'],
            },
        ),
        migrations.RenameModel(
            old_name='SeancesFilms',
            new_name='SeancesFilm',
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['libelle'], 'verbose_name': 'Genre'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ['libelle'], 'verbose_name': 'Version'},
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='libelle_genre',
            new_name='libelle',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='libelle_version',
            new_name='libelle',
        ),
        migrations.AlterField(
            model_name='film',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cineseries.Classification'),
        ),
        migrations.DeleteModel(
            name='Classification_CSA',
        ),
    ]
