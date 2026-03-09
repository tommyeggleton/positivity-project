from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SourceOfGratitude",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
            ],
            options={
                "verbose_name": "Source of Gratitude",
                "verbose_name_plural": "Sources of Gratitude",
            },
        ),
    ]
