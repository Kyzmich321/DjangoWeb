from django.db import models


class CaruselModel(models.Model):
    carusel_img = models.ImageField(upload_to='sliderimg/')
    carusel_title = models.CharField(max_length=200, verbose_name="Title")
    carusel_text = models.CharField(max_length=200, verbose_name="Text")
    carusel_css = models.CharField(max_length=200, null=True, default='♥', verbose_name="Css style")

    def __str__(self):
        return self.carusel_title

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
