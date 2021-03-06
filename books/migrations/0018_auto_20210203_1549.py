# Generated by Django 3.1.6 on 2021-02-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('isbn', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pages', models.PositiveIntegerField(default=200)),
                ('stock_count', models.PositiveIntegerField(default=30)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
        migrations.AlterField(
            model_name='location',
            name='group',
            field=models.CharField(choices=[('Office', 'Office'), ('Industrial', 'Industrial'), ('Retail', 'Retail'), ('Leisure', 'Leisure')], max_length=255),
        ),
    ]
