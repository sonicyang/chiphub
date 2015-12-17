from django.db import models

class GClasses(models.Model):
    mname = models.CharField(max_length = 60, null=True, blank=True)
    sname = models.CharField(max_length = 60, null=True, blank=True)

    class Meta:
        verbose_name = "GClass"

    def __str__(self):
        return "GClass No." + str(self.pk).zfill(4) + " / Name: " + str(self.mname) + " / Sub: " + str(self.sname)

class GComponents(models.Model):
    common_name = models.CharField(max_length = 60, null=True, blank=True)
    manufacturer = models.CharField(max_length = 60, null=True, blank=True)
    ctype = models.ForeignKey(GClasses)

    class Meta:
        verbose_name = "GComponent"

    def __str__(self):
        return "GComponent No." + str(self.pk).zfill(5) + " / CName: " + str(self.common_name) + " / Manufacturer: " + str(self.manufacturer)

def sanity_injection(text):
    pass

def fuzzy_search_component(text):
    #XXX: Apply to every column
    result = []
    for x in text.split(" "):
        result.append(GComponents.objects.raw("SELECT * FROM \"ComponentLibrary_gcomponents\" WHERE common_name %% '{0}' LIMIT 100".format(text)))

    return result
