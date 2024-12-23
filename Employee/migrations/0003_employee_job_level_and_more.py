# Generated by Django 5.1.3 on 2024-11-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_remove_employee_performance_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Mid-Level', 'Mid-Level'), ('Senior', 'Senior'), ('Head', 'Head')], default='Junior', max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emergency_contact_phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media/default.jpg', upload_to='profile_pictures/'),
        ),
    ]
