# Generated by Django 4.2.6 on 2023-12-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]
