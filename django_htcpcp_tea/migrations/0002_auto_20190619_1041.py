# Generated by Django 2.2.2 on 2019-06-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_htcpcp_tea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='name',
            field=models.CharField(help_text='The name of this beverage addition as it would appear in the HTCPCP Accept-Additions header field.', max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='pot',
            name='brew_coffee',
            field=models.BooleanField(default=True, help_text='Can this pot brew coffee?', verbose_name='able to brew coffee'),
        ),
        migrations.AlterField(
            model_name='pot',
            name='name',
            field=models.CharField(help_text='The name of this pot, e.g. "Joe\'s Joe Jar" or "Breville (R) BTM800XL"', max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='pot',
            name='supported_additions',
            field=models.ManyToManyField(blank=True, related_name='pot_list', to='django_htcpcp_tea.Addition'),
        ),
        migrations.AlterField(
            model_name='pot',
            name='supported_teas',
            field=models.ManyToManyField(blank=True, related_name='pot_list', to='django_htcpcp_tea.TeaType'),
        ),
    ]
