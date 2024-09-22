# Generated by Django 5.1.1 on 2024-09-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(help_text='Загрузите изображение', upload_to='catalog/image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]