# Generated by Django 5.0.7 on 2024-12-28 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_wishlist_product'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='dealoftheday',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='productreview',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='tag',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='topshopper',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='wishlist',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='dealoftheday',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='topshopper',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='deactivated_at',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='deactivated_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='deactivation_reason',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='updated_by',
        ),
    ]
