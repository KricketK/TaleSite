# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Character')),
            ],
            bases=('character.character',),
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Character')),
            ],
            bases=('character.character',),
        ),
        migrations.CreateModel(
            name='Wizard',
            fields=[
                ('character_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Character')),
            ],
            bases=('character.character',),
        ),
        migrations.CreateModel(
            name='Alchemist',
            fields=[
                ('scholar_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Scholar')),
            ],
            bases=('character.scholar',),
        ),
        migrations.CreateModel(
            name='Assassin',
            fields=[
                ('fighter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Fighter')),
            ],
            bases=('character.fighter',),
        ),
        migrations.CreateModel(
            name='Barbarian',
            fields=[
                ('fighter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Fighter')),
            ],
            bases=('character.fighter',),
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('wizard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Wizard')),
            ],
            bases=('character.wizard',),
        ),
        migrations.CreateModel(
            name='Shaman',
            fields=[
                ('wizard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='character.Wizard')),
            ],
            bases=('character.wizard',),
        ),
    ]
