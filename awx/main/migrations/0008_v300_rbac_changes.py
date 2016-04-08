# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import taggit.managers
import awx.main.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_v300_active_flag_removal'),
    ]

    operations = [
        migrations.RenameField(
            'Organization',
            'admins',
            'deprecated_admins',
        ),
        migrations.RenameField(
            'Organization',
            'users',
            'deprecated_users',
        ),
        migrations.RenameField(
            'Team',
            'users',
            'deprecated_users',
        ),
        migrations.RenameField(
            'Team',
            'projects',
            'deprecated_projects',
        ),

        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('description', models.TextField(default=b'', blank=True)),
                ('name', models.CharField(max_length=512)),
                ('singleton_name', models.TextField(default=None, unique=True, null=True, db_index=True)),
                ('object_id', models.PositiveIntegerField(default=None, null=True)),
                ('ancestors', models.ManyToManyField(related_name='descendents', to='main.Role')),
                ('content_type', models.ForeignKey(default=None, to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(related_name="{u'class': 'role', u'app_label': 'main'}(class)s_created+", on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('members', models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name="{u'class': 'role', u'app_label': 'main'}(class)s_modified+", on_delete=django.db.models.deletion.SET_NULL, default=None, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('parents', models.ManyToManyField(related_name='children', to='main.Role')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'db_table': 'main_rbac_roles',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('auto_generated', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField(default=None)),
                ('create', models.IntegerField(default=0)),
                ('read', models.IntegerField(default=0)),
                ('write', models.IntegerField(default=0)),
                ('update', models.IntegerField(default=0)),
                ('delete', models.IntegerField(default=0)),
                ('execute', models.IntegerField(default=0)),
                ('scm_update', models.IntegerField(default=0)),
                ('use', models.IntegerField(default=0)),
                ('content_type', models.ForeignKey(default=None, to='contenttypes.ContentType')),
                ('role', models.ForeignKey(related_name='permissions', to='main.Role')),
            ],
            options={
                'db_table': 'main_rbac_permissions',
                'verbose_name_plural': 'permissions',
            },
        ),
        migrations.AddField(
            model_name='credential',
            name='owner_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='credential',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='credential',
            name='usage_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='group',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='group',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='group',
            name='executor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='group',
            name='updater_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='executor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='updater_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='custominventoryscript',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='custominventoryscript',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='custominventoryscript',
            name='member_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='executor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='organization',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='organization',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='organization',
            name='member_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='project',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='project',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='project',
            name='member_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='project',
            name='scm_update_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='team',
            name='admin_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='team',
            name='auditor_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AddField(
            model_name='team',
            name='member_role',
            field=awx.main.fields.ImplicitRoleField(related_name='+', to='main.Role', null=b'True'),
        ),
        migrations.AlterIndexTogether(
            name='rolepermission',
            index_together=set([('content_type', 'object_id')]),
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='projects',
            new_name='deprecated_projects',
        ),
        migrations.AlterField(
            model_name='organization',
            name='deprecated_projects',
            field=models.ManyToManyField(related_name='deprecated_organizations', to='main.Project', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='organization',
            field=models.ForeignKey(related_name='projects', to='main.Organization', blank=True, null=True),
        ),
        migrations.RenameField(
            'Credential',
            'team',
            'deprecated_team',
        ),
        migrations.RenameField(
            'Credential',
            'user',
            'deprecated_user',
        ),
        migrations.AlterField(
            model_name='organization',
            name='deprecated_admins',
            field=models.ManyToManyField(related_name='deprecated_admin_of_organizations', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='deprecated_users',
            field=models.ManyToManyField(related_name='deprecated_organizations', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='deprecated_users',
            field=models.ManyToManyField(related_name='deprecated_teams', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='credential',
            unique_together=set([]),
        ),
    ]