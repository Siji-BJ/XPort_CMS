# Generated by Django 3.0.7 on 2020-06-26 04:52

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('menus', '0006_remove_footer_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='sort_order',
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page_title', models.CharField(blank=True, max_length=50, null=True)),
                ('new_tab', models.BooleanField(blank=True, default=False)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='menus.MenuItem')),
                ('sub_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
