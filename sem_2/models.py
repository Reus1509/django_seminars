from django.db import models


class Coin(models.Model):
    side = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Выпала {self.side} в {self.time_created}!'

    @staticmethod
    def get_data(num):
        coins = Coin.objects.all()[:num]
        coins_dict = {
            'Орел': [],
            'Решка': []
        }
        for i in coins:
            if i.side == 1:
                coins_dict['Орел'].append(i.time_created)
            elif i.side == 0:
                coins_dict['Решка'].append(i.time_created)

        return f"За последние {num} бросков орел выпал: {len(coins_dict['Орел'])}, решка выпала: {len(coins_dict['Решка'])} "


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'Имя: {self.name} Фамилия: {self.last_name} Почта: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'
