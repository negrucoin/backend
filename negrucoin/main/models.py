from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from settings import MONEY_PER_MINUTE

User = get_user_model()


class Client(models.Model):
    """Simple client model, that expands default User model."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client',
        verbose_name='Пользователь'
    )
    ACCOUNT_TYPES = [
        ('default', 'Пользователь'),
        ('manager', 'Менеджер'),
        ('admin', 'Админ'),
    ]
    account_type = models.CharField('Тип аккаунта', max_length=255, choices=ACCOUNT_TYPES, default='default')
    money_profit = models.BigIntegerField('Профит монет', default=0)
    rubles = models.DecimalField('Кол-во рублей', max_digits=9, decimal_places=2, default=0)

    def calculate_money(self) -> int:
        """Calculate client's money.

        We're not using something like celery to increase client's money every
        second. I think it's unnecessary, let's just calculate money in real-time,
        from the moment the client registers. And take into account the user's expenses.
        """

        now = timezone.now()

        # Wooow, client travels back in time!
        assert now > self.user.date_joined

        client_lifetime = (now - self.user.date_joined).total_seconds()
        earned_money = client_lifetime // 60 * MONEY_PER_MINUTE

        return int(earned_money + self.money_profit)


class MoneyTransfer(models.Model):
    """Models for save info about p2p money transfers."""

    sender = models.ForeignKey(
        Client,
        related_name='sent_money_transfers',
        on_delete=models.PROTECT,
        verbose_name='Отправитель'
    )
    receiver = models.ForeignKey(
        Client,
        related_name='received_money_transfers',
        on_delete=models.PROTECT,
        verbose_name='Получатель'
    )
    money_count = models.BigIntegerField('Кол-во монет')
    created_at = models.DateTimeField('Дата', auto_now_add=True)


class MoneySaleOffer(models.Model):
    """Entity for defining a "stack" of money for sale.

    The client can put up for sale a certain number of coins at a certain price.
    The number of coins and the price for them is determined by the client himself.
    To save this information, this model was created.
    """

    seller = models.ForeignKey(
        Client,
        related_name='money_sale_lots',
        on_delete=models.CASCADE,
        verbose_name='Продавец'
    )
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('closed', 'Закрыт'),
        ('sold_out', 'Раскуплен'),
    ]
    status = models.CharField('Статус', max_length=255, choices=STATUS_CHOICES, default='created')
    money = models.BigIntegerField('Кол-во монет в предложении')
    price = models.DecimalField('Цена всего предложения (в рублях)', max_digits=9, decimal_places=2)
    created_at = models.DateTimeField('Дата', auto_now_add=True)

    @property
    def one_coin_price(self) -> float:
        return self.price / self.money


class MoneyPurchase(models.Model):
    """Models for save info about money purchases."""

    seller = models.ForeignKey(
        Client,
        related_name='sold_money_purchases',
        on_delete=models.PROTECT,
        verbose_name='Продавец'
    )
    customer = models.ForeignKey(
        Client,
        related_name='bought_money_purchases',
        on_delete=models.PROTECT,
        verbose_name='Покупатель'
    )
    money_sale_lot = models.ForeignKey(
        MoneySaleOffer,
        related_name='money_purchases',
        on_delete=models.PROTECT,
        verbose_name='Предложение продажи монет'
    )
    money = models.BigIntegerField('Кол-во купленных монет')
    rubles = models.DecimalField('Кол-во потраченных рублей', max_digits=9, decimal_places=2)
    created_at = models.DateTimeField('Дата', auto_now_add=True)
