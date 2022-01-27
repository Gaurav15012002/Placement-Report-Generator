# Generated by Django 3.2.6 on 2022-01-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PMS_website', '0008_alter_summary_detail_eligible_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='higher_study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('COMP', 'COMP'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('ETRX', 'ETRX'), ('AI&DS', 'AI & DS')], default='COMP', max_length=255)),
                ('study_year', models.CharField(max_length=4)),
                ('student_name', models.CharField(max_length=255)),
                ('qualifying_exam', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
            ],
        ),
    ]
