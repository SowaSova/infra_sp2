# Generated by Django 2.2.16 on 2022-08-22 20:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reviews", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="title",
            field=models.ForeignKey(
                db_constraint=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="reviews.Title",
            ),
        ),
        migrations.AddField(
            model_name="genretitle",
            name="genre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reviews.Genre"
            ),
        ),
        migrations.AddField(
            model_name="genretitle",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reviews.Title"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="review",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="reviews.Review",
            ),
        ),
        migrations.AddConstraint(
            model_name="title",
            constraint=models.CheckConstraint(
                check=models.Q(year__lte=2022), name="year_lte_now"
            ),
        ),
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(
                fields=("title", "author"), name="unique author review"
            ),
        ),
    ]
