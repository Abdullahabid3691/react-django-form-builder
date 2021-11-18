# Generated by Django 3.2.9 on 2021-11-18 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('TEXT', 'Text Field'), ('EMAIL', 'Email Field'), ('MULTIPLE', 'Multiple Choices'), ('DROPDOWN', 'Dropdown')], default='TEXT', max_length=10)),
                ('question', models.CharField(max_length=10000)),
                ('choices', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responder', to=settings.AUTH_USER_MODEL)),
                ('response', models.ManyToManyField(related_name='response', to='form_builder.Answer')),
                ('response_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_to', to='form_builder.form')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='questions',
            field=models.ManyToManyField(related_name='questions', to='form_builder.Questions'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_to', to='form_builder.questions'),
        ),
    ]
