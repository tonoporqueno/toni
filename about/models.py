from django.db import models

# Create your models here


class tessio(models.Model):
    temperature = models.FloatField()

    class Meta:
        verbose_name = "Tejido"
        verbose_name_plural = "Tejidos"

    def __str__(self):
        return str(self.temperature)

   # def get_absolute_url(self):
    #    return reverse("tablacanotenido_detail", kwargs={"pk": self.pk})
