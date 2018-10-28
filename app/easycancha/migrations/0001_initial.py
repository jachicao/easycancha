# Generated by Django 2.1.2 on 2018-10-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('easycancha_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubSport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easycancha.Club')),
            ],
        ),
        migrations.CreateModel(
            name='OneTimeReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('clubsport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easycancha.ClubSport')),
            ],
        ),
        migrations.CreateModel(
            name='RecurrentReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.IntegerField()),
                ('minute', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('clubsport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easycancha.ClubSport')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='recurrentreservation',
            name='weekday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easycancha.Weekday'),
        ),
        migrations.AddField(
            model_name='clubsport',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easycancha.Sport'),
        ),
        migrations.AlterUniqueTogether(
            name='clubsport',
            unique_together={('club', 'sport')},
        ),
    ]
