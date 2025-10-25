from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class CategoryStatus(models.IntegerChoices):
    publish = 1 ,("نمایش")
    draft = 2 ,("عدم نمایش")


class CategoryPost(models.Model):
    """ Categories of articles with the status of display and non-display by the admin"""
    title = models.CharField(_('عنوان'),max_length=120)
    status = models.IntegerField(_('وضعیت نمایش'),choices=CategoryStatus.choices,default=CategoryStatus.publish.value)
    created_date = models.DateTimeField(_('تاریخ ایجاد'),auto_now_add=True)
    
    
class CategoryGallery(models.Model):
    """ Categories of Gallery with the status of display and non-display by the admin"""
    title = models.CharField(_('عنوان'),max_length=120)
    status = models.IntegerField(_('وضعیت نمایش'),choices=CategoryStatus.choices,default=CategoryStatus.publish.value)
    created_date = models.DateTimeField(_('تاریخ ایجاد'),auto_now_add=True)
    

class Post(models.Model):
    """   Model blog articles  """
    title = models.CharField(_('عنوان'),max_length=120)
    image = models.ImageField(_('تصویر پست'),upload_to='Post/image')
    description = models.TextField(_('توضیحات'))
    category = models.ForeignKey(CategoryPost,verbose_name='دسته بندی')
    status = models.BooleanField(_('وضعیت نمایش'))
    created_date = models.DateTimeField(_('تاریخ ایجاد'),auto_now_add=True)
    updated_date = models.DateTimeField(_('تاریخ بروزرسانی'),auto_now=True)
    
    def __str__(self):
        return self.title
    
    def show_image(self):
        """To display images in the management panel"""
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="78 px" height="50" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"


    class Meta:
        verbose_name_plural = "پست ها"
        verbose_name = "پست"
        ordering = ['-created']
        

class Gallery(models.Model):
    """  Portfolio image gallery  """
    title = models.CharField(_('عنوان'),max_length=120)
    image = models.ImageField(_('تصویر پست'),upload_to='Gallery/image')
    category = models.ForeignKey(CategoryGallery,verbose_name='دسته بندی گالری ها')
    status = models.BooleanField(_('وضعیت نمایش'))
    created_date = models.DateTimeField(_('تاریخ ایجاد'),auto_now_add=True)
    updated_date = models.DateTimeField(_('تاریخ بروزرسانی'),auto_now=True)

    def __str__(self):
        return self.title
    
    def show_image(self):
        """To display images in the management panel"""
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="78 px" height="50" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"
    
    class Meta:
        verbose_name_plural = "پست ها"
        verbose_name = "پست"
        ordering = ['-created']
        



