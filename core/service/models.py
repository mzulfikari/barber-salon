from django.db import models
from django.utils.translation import gettext_lazy as _


SERVICES = [
    ('HAIRCUT', 'کوتاهی و استایل مو'),
    ('HAIRCARE', 'احیا و مراقبت مو'),
    ('HAIRCOLOR', 'رنگ، مش و هایلایت مو'),
    ('HAIRSTYLE', 'طراحی مدل مو و براشینگ'),

    ('BEARD_TRIM', 'اصلاح و فرم‌دهی ریش'),
    ('BEARD_DESIGN', 'طراحی و خط‌گیری ریش و سبیل'),
    ('BEARD_CARE', 'احیا و کراتینه ریش'),

    ('FACIAL_BASIC', 'پاکسازی و مراقبت پوست'),
    ('FACIAL_PRO', 'فیشیال تخصصی مردانه'),
    ('EYEBROW', 'اصلاح و فرم‌دهی ابرو'),
    ('MAKEUP_GROOM', 'گریم و آرایش داماد'),

    ('MASSAGE', 'ماساژ بدن (ریلکسی / درمانی)'),
    ('BODY_CARE', 'اسکراب و بخور بدن'),
    ('EPILATION', 'اپیلاسیون بدن'),

    ('GROOM_PACK', 'پکیج کامل داماد / VIP'),
    ('VIP', 'خدمات ویژه و لوکس'),
    ('SPECIAL', 'خدمات خاص و مدرن (نانو تراپی، کاشت مو و...)'),
]


class Service(models.Model):
    """ 
    Registration of hairdressing services with features of service time,
    price,
    description and image,
    which is available for each separate reporting service
    """
    barber = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    name = models.CharField(_('عنوان خدمت'),choices=SERVICES,max_length=50,related_name='name_service')
    time = models.TimeField(_('زمان خدمت'))
    image = models.ImageField(_('تصویر خدمت'),upload_to='service/image')
    price = models.IntegerField(_('هزینه خدمت'))
    description = models.TextField(_('توضیحات'))
    status = models.BooleanField(_('وضعیت'))
    create_date = models.DateTimeField(_('زمان اضافه کردن سرویس'),auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "خدمات"
        verbose_name = "خدمت"


class ReservationDay(models.Model):
    """ Define the day in the database """
    day = models.DateField(_('روز'),unique=True)
    
    def __str__(self):
     return f"{self.day}"
    

class Reservation(models.Model):
    """ 
    Scheduling structure with the ability to choose the day of the appointment,
    the hairdresser, the type of service, time and customer information
    """
    day = models.ForeignKey(ReservationDay,verbose_name='نوبت های روز')
    barber = models.ForeignKey('accounts.Profile',on_delete=models.CASCADE)
    service = models.ForeignKey(Service,verbose_name='خدمت')
    time = models.DateTimeField(_('زمان ثبت نوبت'),auto_now_add=True)
    full_name_customer = models.CharField(_('نام و نام خانوادگی مشتری'),max_length=100)
    phone_customer = models.CharField(_('موبایل مشتری'),max_length=15,validators=[])

    
    def __str__(self):
     return f"{self.day}  {self.service} "
 
    class Meta:
        unique_together = ('time','barber')