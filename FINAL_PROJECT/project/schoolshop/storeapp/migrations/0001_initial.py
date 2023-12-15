# Generated by Django 4.2.6 on 2023-12-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(choices=[('commerce', 'Commerce'), ('science', 'Science'), ('arts', 'Arts')], max_length=50)),
                ('course', models.CharField(blank=True, choices=[], max_length=50)),
                ('purpose', models.CharField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')], max_length=50)),
                ('materials_provide', models.ManyToManyField(blank=True, to='storeapp.material')),
            ],
        ),
    ]
