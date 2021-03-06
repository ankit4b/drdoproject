# Generated by Django 3.0.4 on 2020-04-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_recruitment_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('publish_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='recruitment_article',
        ),
    ]
