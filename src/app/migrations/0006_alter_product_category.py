# Generated by Django 4.0.5 on 2022-07-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('W', 'Watch'), ('P', 'Printer'), ('F', 'Fan'), ('EB', 'Earbuds'), ('C', 'Camera'), ('O', 'Oil'), ('SH', 'Shower'), ('MU', 'Museli')], max_length=2),
        ),
    ]
