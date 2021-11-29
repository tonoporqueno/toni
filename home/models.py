from django.db import models

# Create your models here
# name = models.CharField(max_length=50)


class Paciente(models.Model):
    models.CharField()
    # name = models.CharField(max_length=50,)

    class Meta:
        verbose_name = ("paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return self.name


class tessio(models.Model):
    temperature = models.FloatField(verbose_name="temperatura")
    color = models.FloatField()
    inflamacion = models.FileField(verbose_name="inflamación")
    name = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    # name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'tejido'
        verbose_name_plural = 'Tejidos'

        def __str__(self):
            return 'temperatura' + str(self.temperature)+' color:' + str(self.color)
