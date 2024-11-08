# Generated by Django 5.0.9 on 2024-11-07 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glosa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_glosa', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('rejected_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='GlosaForErrorOFfactoring',
            fields=[
                ('glosa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='glosasApi.glosa')),
                ('type_error', models.CharField(max_length=100)),
            ],
            bases=('glosasApi.glosa',),
        ),
        migrations.CreateModel(
            name='GlosaForLessDocumentation',
            fields=[
                ('glosa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='glosasApi.glosa')),
                ('missed_documents', models.TextField()),
            ],
            bases=('glosasApi.glosa',),
        ),
    ]
