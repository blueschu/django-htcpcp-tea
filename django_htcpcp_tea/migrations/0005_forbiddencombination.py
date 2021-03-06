# Generated by Django 2.2.2 on 2019-07-04 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_htcpcp_tea', '0004_addition_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForbiddenCombination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=180)),
                ('additions', models.ManyToManyField(related_name='forbidden_combinations', to='django_htcpcp_tea.Addition')),
                ('tea', models.ForeignKey(blank=True, help_text='The type of tea that this forbidden combination applies to. Leave blank to apply to all beverages.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forbidden_combinations', to='django_htcpcp_tea.TeaType')),
            ],
        ),
    ]
