# Generated by Django 4.2.7 on 2025-01-14 03:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('points_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rebounds_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('assists_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('steals_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('blocks_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('turnovers_per_game', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('field_goal_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('three_point_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('free_throw_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('efficiency_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('true_shooting_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('usage_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defensive_score', models.IntegerField()),
                ('passing_score', models.IntegerField()),
                ('scoring_score', models.IntegerField()),
                ('iq_score', models.IntegerField()),
                ('final_grade', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluations.player')),
            ],
        ),
    ]
