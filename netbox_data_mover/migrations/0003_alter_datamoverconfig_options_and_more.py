# Generated by Django 5.0.9 on 2024-11-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_data_mover', '0002_remove_datasourcemodel_tags_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datamoverconfig',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='datamoverdatasource',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='datamoverconfig',
            name='fetch_data_definition',
        ),
        migrations.RemoveField(
            model_name='datamoverconfig',
            name='transformations',
        ),
        migrations.RemoveField(
            model_name='datamoverdatasource',
            name='api_url',
        ),
        migrations.RemoveField(
            model_name='datamoverdatasource',
            name='auth_details',
        ),
        migrations.AddField(
            model_name='datamoverconfig',
            name='destination_endpoint',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='datamoverconfig',
            name='mappings',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='datamoverconfig',
            name='source_endpoint',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='auth_args',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='auth_function',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='auth_method',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='base_urls',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='create_function',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='fetch_function',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='find_function',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='module',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='datamoverdatasource',
            name='update_function',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datamoverconfig',
            name='schedule',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='DataMoverJob',
        ),
    ]