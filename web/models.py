from django.db import models



# Create your models here.
class Slider(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")


    class Meta:
        db_table = 'web_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['-id']


    def __str__(self):
        return self.title

# Legacy
class Legacy(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")


    class Meta:
        db_table = 'web_legacy'
        verbose_name = 'legacy'
        verbose_name_plural = 'legacies'
        ordering = ['-id']


    def __str__(self):
        return self.title
    
    

    

# about box   
class Aboutbox(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")


    class Meta:
        db_table = 'web_aboutbox'
        verbose_name = 'aboutbox'
        verbose_name_plural = 'aboutboxes'
        ordering = ['-id']


    def __str__(self):
        return self.title

# product category
class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="slider")
    description = models.TextField()
    



    class Meta:
        db_table = 'web_productcategory'
        verbose_name = 'productcategory'
        verbose_name_plural = 'productcategorie'
        ordering = ['-id']


    def __str__(self):
        return self.name


# product features
class ProductFeature(models.Model):
    name = models.CharField(max_length=255)



    class Meta:
        db_table = 'web_productfeature'
        verbose_name = 'productfeature'
        verbose_name_plural = 'productfeatures'
        ordering = ['-id']


    def __str__(self):
        return self.name

 

# product   
class Product(models.Model):

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")
    brandlogo = models.ImageField(upload_to="slider")
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    features  = models.ManyToManyField(ProductFeature)   



    class Meta:
        db_table = 'web_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-id']


    def __str__(self):
        return self.title        




# gallery category
class GalleryCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")


    class Meta:
        db_table = 'web_gallerycategory'
        verbose_name = 'gallerycategory'
        verbose_name_plural = 'gallerycategories'
        ordering = ['-id']


    def __str__(self):
        return self.name
    
 # gallery image
class Galleryimage(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider")
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE ,blank=True, null=True)



    class Meta:
        db_table = 'web_galleryimage'
        verbose_name = 'galleryimage'
        verbose_name_plural = 'galleryimages'
        ordering = ['-id']


    def __str__(self):
        return self.name

