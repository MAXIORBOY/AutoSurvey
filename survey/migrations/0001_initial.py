# Generated by Django 3.1.2 on 2020-10-10 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey_name', models.CharField(max_length=100, unique=True)),
                ('survey_description', models.CharField(max_length=500)),
                ('survey_photo_link', models.CharField(max_length=300)),
                ('survey_photo_orientation', models.CharField(choices=[('horizontal', 'Horizontal'), ('portrait', 'Portrait')], default='horizontal', max_length=50)),
                ('survey_type', models.CharField(choices=[('single_choice', 'Single choice'), ('multi_choice', 'Multi choice'), ('answer_comparasion', 'Answer comparasion')], max_length=50)),
                ('survey_type_parameters', models.IntegerField(default=2)),
                ('survey_user_has_one_vote', models.BooleanField(default=True)),
                ('survey_creation_date', models.DateTimeField(auto_now_add=True)),
                ('survey_completion_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_ip', models.GenericIPAddressField(editable=False)),
                ('survey_name', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_name', models.CharField(max_length=100)),
                ('answer_description', models.CharField(blank=True, max_length=200, null=True)),
                ('answer_photo_link', models.CharField(blank=True, max_length=300, null=True)),
                ('answer_photo_orientation', models.CharField(choices=[('horizontal', 'Horizontal'), ('portrait', 'Portrait')], default='horizontal', max_length=50)),
                ('votes', models.IntegerField(default=0)),
                ('answer_creation_date', models.DateTimeField(auto_now_add=True)),
                ('survey_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
            ],
        ),
    ]
