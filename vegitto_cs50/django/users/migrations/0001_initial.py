# Generated by Django 3.1.12 on 2021-10-04 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='last name')),
                ('username', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='username')),
                ('password', models.CharField(blank=True, max_length=165, null=True, verbose_name='password')),
                ('mobile_number', models.CharField(blank=True, error_messages={'unique': 'A user with this mobile number already exists.'}, help_text='(09*********)phone number', max_length=20, null=True, unique=True, validators=[users.models.UnicodeMobileNumberValidator()], verbose_name='mobile number')),
                ('email', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='email address')),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'man'), (1, 'woman')], null=True, verbose_name='gender')),
                ('type', models.CharField(blank=True, choices=[('chief', 'chief'), ('doctor', 'doctor')], max_length=20, null=True, verbose_name='type')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name=' is staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('joined_at', models.DateTimeField(auto_now_add=True, verbose_name='joined at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=users.models.user_profile_image_path, verbose_name='profile image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.province')),
            ],
        ),
    ]
