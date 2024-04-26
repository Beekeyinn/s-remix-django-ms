# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import uuid

from django.db import models


class Profile(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4())
    sessionid = models.OneToOneField(
        "Session", models.DO_NOTHING, db_column="sessionId"
    )  # Field name made lowercase.
    first_name = models.TextField()
    last_name = models.TextField()
    shop_name = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Profile"


class Session(models.Model):
    id = models.TextField(primary_key=True)
    shop = models.TextField()
    state = models.TextField()
    isonline = models.BooleanField(db_column="isOnline")  # Field name made lowercase.
    scope = models.TextField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    accesstoken = models.TextField(
        db_column="accessToken"
    )  # Field name made lowercase.
    userid = models.BigIntegerField(
        db_column="userId", blank=True, null=True
    )  # Field name made lowercase.
    paid = models.BooleanField()
    subscription = models.JSONField(blank=True, null=True)
    createdat = models.DateTimeField(
        db_column="createdAt"
    )  # Field name made lowercase.
    updatedat = models.DateTimeField(
        db_column="updatedAt"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Session"


class Settings(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4())
    logrocket = models.BooleanField()
    logrocket_key = models.TextField(blank=True, null=True)
    crisp = models.BooleanField()
    crispt_key = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Settings"


class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = "_prisma_migrations"
