from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_client_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='heading',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
