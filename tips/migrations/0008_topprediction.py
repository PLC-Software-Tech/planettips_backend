# Generated by Django 4.2.3 on 2023-08-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0007_alter_matchtips_play_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(blank=True, max_length=255, null=True)),
                ('league_short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('league_icon', models.CharField(max_length=255, null=True)),
                ('home_team', models.CharField(blank=True, max_length=255, null=True)),
                ('away_team', models.CharField(blank=True, max_length=255, null=True)),
                ('home_team_probability', models.IntegerField(blank=True, null=True)),
                ('away_team_probability', models.IntegerField(null=True)),
                ('draw_probability', models.IntegerField(null=True)),
                ('prediction', models.CharField(max_length=255, null=True)),
                ('correct_score', models.CharField(max_length=255, null=True)),
                ('avg_goals', models.CharField(max_length=255, null=True)),
                ('odds', models.CharField(max_length=255, null=True)),
                ('live_odds', models.CharField(max_length=255, null=True)),
                ('score', models.CharField(max_length=255, null=True)),
                ('play_date', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
