# Generated by Django 3.2 on 2021-04-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20210428_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['ordering'], 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='screen',
            name='categories',
        ),
        migrations.CreateModel(
            name='CategoryLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column', models.IntegerField(choices=[(1, 'Column 1'), (2, 'Column 2'), (3, 'Column 3')], default=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layouts', to='menu.category')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.screen')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='layouts',
            field=models.ManyToManyField(through='menu.CategoryLayout', to='menu.Category'),
        ),
    ]