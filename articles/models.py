from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Thematic(models.Model):
    tag = models.CharField(max_length=10)
    tags = models.ManyToManyField(
        Article,
        through='Membership',
        through_fields=('tag', 'article')
    )

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тэги'
        verbose_name_plural = 'Тэг'

    def __str__(self):
        return self.tag


class Membership(models.Model):
    tag = models.ForeignKey(Thematic, on_delete=models.CASCADE, verbose_name='РАЗДЕЛ')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    main_tag = models.BooleanField(default=False, verbose_name='Основной')
