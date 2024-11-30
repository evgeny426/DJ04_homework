from django.db import models

# Создайте проект с именем movie_project и приложение в нем films. Создайте модель(таблицу) в которой будет поле для названия фильма, поле для описание фильма и поле для отзыва.
#
# Создайте две html страницы, на одной из которых нужно заполнить 3 поля и отправить эту информацию в базу данных, а на второй будет публиковаться информация которую вы записали в базу данных.


class Films(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
