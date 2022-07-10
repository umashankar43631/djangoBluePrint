from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    dateOfBirth = models.DateField(null= True)
    slug = models.SlugField(null=False, default="", db_index= True,)

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.username)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username

"""
    To create
            store the modelName(attribute = value)
            variable.save
        Another Way
            modelName.objects.create(attribute= value)
    To update the data in database
        save the record in a variable, modelName.objects.all()
        update the record value
        then variable.save()
    To delete a record in a database
        store the record in a variable, modelName.objects.all()[0]
        variable.delete()   
    To Retrieve a single Record(one record only) by filtering(should match only one record)
        modelName.objects.get(attribute=value)// you can search by id also
    To Retrieve Multiple Records by filtering
        modelName.objects.filter(attribute = value )
        modelName.objects.filterr(attribute__lt = value)
        modelName.objects.filterr(attribute__lte = value)(Field Lookups they are called)
        modelName.objects.filterr(attribute__contains = value)
        modelName.objects.filterr(attribute__icontains = value)// case insensitive
    To get records with mulitple joining queries(OR(|) and AND(,))
        from django.db.models import Q
        modelName.objects.filter(Q(attribute_lte = value) | Q(attribute_contains = value))
        We can Further filter Filtered Results by using variableName.filter(attribute_name = value)
    To increase performance of an model, you need to store query in a variable so that if 
    we print that variable multiple times , database only hit once.
    To insert multiple records in a single query
            objs = Entry.objects.bulk_create([
        ...     Entry(headline='This is a test'),
        ...     Entry(headline='This is only a test'),
        ... ])
    To update multiple records in a single query
                    >>> objs = [
        ...    Entry.objects.create(headline='Entry 1'),
        ...    Entry.objects.create(headline='Entry 2'),
        ... ]
        >>> objs[0].headline = 'This is entry 1'
        >>> objs[1].headline = 'This is entry 2'
        >>> Entry.objects.bulk_update(objs, ['headline'])
        2
"""
    
        
""" Super user 
        username: shankar8331
        email: .mulakalapalli@gmail.com
        password: Uma12345
"""