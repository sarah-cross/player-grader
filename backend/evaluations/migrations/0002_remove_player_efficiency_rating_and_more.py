# Generated by Django 4.2.7 on 2025-01-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='efficiency_rating',
        ),
        migrations.RemoveField(
            model_name='player',
            name='field_goal_percentage',
        ),
        migrations.RemoveField(
            model_name='player',
            name='free_throw_percentage',
        ),
        migrations.RemoveField(
            model_name='player',
            name='three_point_percentage',
        ),
        migrations.RemoveField(
            model_name='player',
            name='true_shooting_percentage',
        ),
        migrations.RemoveField(
            model_name='player',
            name='usage_percentage',
        ),
        migrations.AddField(
            model_name='player',
            name='efficiency',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='field_goals_att',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='field_goals_made',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='free_throws_att',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='free_throws_made',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='three_points_att',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='player',
            name='three_points_made',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='assists_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='blocks_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='points_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(default='Unknown', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='rebounds_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='steals_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='turnovers_per_game',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
