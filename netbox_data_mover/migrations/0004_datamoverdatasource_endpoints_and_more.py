# Generated by Django 5.0.9 on 2024-11-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_data_mover', '0003_alter_datamoverconfig_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamoverdatasource',
            name='endpoints',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='auth_function',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='auth_method',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='create_function',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='fetch_function',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='find_function',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='datamoverdatasource',
            name='update_function',
            field=models.TextField(null=True),
        ),
    ]