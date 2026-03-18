from django.db import models


class Profile(models.Model):
    """Asosiy profil ma'lumotlari"""
    full_name = models.CharField(max_length=100, verbose_name="To'liq ism")
    specialty = models.CharField(max_length=150, verbose_name="Mutaxassislik", default="Senior Full-Stack Developer")
    bio = models.TextField(verbose_name="Bio / Haqida")
    photo = models.ImageField(upload_to='profile/', blank=True, null=True, verbose_name="Rasm")
    years_of_experience = models.PositiveIntegerField(default=5, verbose_name="Tajriba yillari")
    projects_count = models.PositiveIntegerField(default=65, verbose_name="Loyihalar soni")
    work_together_url = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="'Birga ishlash' tugmasi URL",
        help_text="Telegram bot yoki email manzilingiz. Masalan: https://t.me/username yoki mailto:email@example.com"
    )

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    """Ish tajribasi (Timeline)"""
    year = models.CharField(max_length=10, verbose_name="Yil")
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Tajriba"
        verbose_name_plural = "Tajribalar"
        ordering = ['order', 'year']

    def __str__(self):
        return f"{self.year} – {self.title}"


class SocialLink(models.Model):
    """Ijtimoiy tarmoqlar"""
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('telegram', 'Telegram'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter / X'),
        ('other', 'Boshqa'),
    ]
    name = models.CharField(max_length=100, verbose_name="Nomi (ko'rsatiladigan)")
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='other', verbose_name="Platforma")
    url = models.URLField(verbose_name="URL manzil")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        ordering = ['order']

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    """Aloqa ma'lumotlari"""
    address = models.CharField(max_length=300, verbose_name="Manzil", blank=True)
    phone = models.CharField(max_length=30, verbose_name="Telefon", blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)

    class Meta:
        verbose_name = "Aloqa ma'lumotlari"
        verbose_name_plural = "Aloqa ma'lumotlari"

    def __str__(self):
        return f"Aloqa: {self.email or self.phone}"
