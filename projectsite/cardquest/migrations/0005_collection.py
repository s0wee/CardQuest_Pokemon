# Generated by Django 5.0 on 2023-12-08 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0004_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cardquest.basemodel')),
                ('collection_date', models.DateField()),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.pokemoncard')),
            ],
            bases=('cardquest.basemodel',),
        ),
    ]
