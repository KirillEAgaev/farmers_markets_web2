from django.db import models
from django.urls import reverse

class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField()
    state = models.ForeignKey('States', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cities'


class Markets(models.Model):
    market_id = models.IntegerField(primary_key=True)
    market_name = models.CharField(blank=True, null=True)
    street = models.CharField(blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='city', blank=True, null=True)
    state = models.ForeignKey('States', models.DO_NOTHING, db_column='state', blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    categories = models.ManyToManyField(Categories, through='MarketsCategories')

    def get_absolute_url(self):
        return reverse('markets-detail', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'markets'


class MarketsCategories(models.Model):
    market_category_id = models.IntegerField(primary_key=True)
    market = models.ForeignKey(Markets, models.DO_NOTHING)
    category = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'markets_categories'


class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    market = models.ForeignKey(Markets, models.DO_NOTHING)
    date_time = models.DateField()
    score = models.SmallIntegerField()
    review = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class States(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_full = models.CharField(blank=True, null=True)
    state_abbr = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'states'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(blank=True, null=True)
    lname = models.CharField(blank=True, null=True)
    username = models.CharField()
    password_hash = models.CharField()

    class Meta:
        managed = False
        db_table = 'users'