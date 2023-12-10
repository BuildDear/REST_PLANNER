# Generated by Django 5.0 on 2023-12-06 11:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_eventcategory_event_attendees_alter_event_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(default='None', related_name='attended_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default='None', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='manager.eventcategory'),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.ManyToManyField(default='None', to='manager.note'),
        ),
    ]
