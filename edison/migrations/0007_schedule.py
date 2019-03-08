# Generated by Django 2.1.4 on 2018-12-14 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edison', '0006_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(choices=[('7:00-8:45', '7:00-8:45'), ('9:00-10:30', '9:00-10:30'), ('10:45-12:15', '10:45-12:15'), ('12:30-14:00', '12:30-14:00')], max_length=30)),
                ('days', models.CharField(choices=[('Pondeli', 'Pondeli'), ('Utery', 'Utery'), ('Streda', 'Streda'), ('Ctvrtek', 'Ctvrtek')], max_length=30)),
                ('students', models.ManyToManyField(to='edison.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edison.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edison.Teacher')),
            ],
            options={
                'verbose_name_plural': 'Schedule',
            },
        ),
    ]
