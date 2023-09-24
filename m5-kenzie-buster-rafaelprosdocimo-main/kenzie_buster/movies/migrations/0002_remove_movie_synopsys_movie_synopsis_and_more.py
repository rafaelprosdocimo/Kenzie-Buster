# Generated by Django 4.2.4 on 2023-08-17 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='synopsys',
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(choices=[('PG', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC-17', 'Nc 17'), ('G', 'G')], default='G', max_length=20),
        ),
        migrations.CreateModel(
            name='MovieOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('buyed_at', models.DateTimeField(auto_now_add=True)),
                ('buyed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_user_order', to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_movie_order', to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_orders',
            field=models.ManyToManyField(related_name='movie_orders', through='movies.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
    ]
