import hashlib

from django.db import models

from main.models import Client
from settings import BILL_ID_SALT


class QIWIBill(models.Model):
    """Special entity to save bills data that arrives from QIWI."""

    client = models.ForeignKey(
        Client,
        related_name='qiwi_bills',
        on_delete=models.PROTECT,
        verbose_name='Кому выставлен'
    )
    STATUS_CHOICES = [
        ('WAITING', 'Ожидается'),
        ('EXPIRED', 'Просрочен'),
        ('REJECTED', 'Отклонен'),
        ('PAID', 'Оплачен'),
    ]
    status = models.CharField('Статус', max_length=255, choices=STATUS_CHOICES, default='WAITING')
    amount = models.DecimalField('Сумма (в рублях)', max_digits=9, decimal_places=2)
    created_at = models.DateTimeField('Дата', auto_now_add=True)
    expired_at = models.DateTimeField('Дата истечения')

    @property
    def bill_id(self) -> str:
        """Unique bill id for QIWI.

        We must generate unique bill id for QIWI bills. Just using `id` field
        from django - not very good, because all clients will see the global number of their bill.
        Haha, I not want to show it, so, we use hash of id with some salt.
        """
        return hashlib.md5(f'{self.id}.{BILL_ID_SALT}'.encode()).hexdigest()


class WithdrawalRequest(models.Model):
    """Withdrawal rubles request from the client.

    Client wants to withdraw his rubles now! Give him his money!
    But wait, we have a 10% commission on withdrawal...

    After 24 hours of request creation the pay can be accepted,
    or not accepted (this manager choice). And if it is accepted
    - Info about this will save to Payment model.
    """

    client = models.ForeignKey(
        Client,
        related_name='withdrawal_requests',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    STATUS_CHOICES = [
        ('PROCESSING', 'В обработке'),
        ('ACCEPTED', 'Принят'),
        ('REJECTED', 'Отклонен'),
    ]
    status = models.CharField('Статус', max_length=255, choices=STATUS_CHOICES, default='PROCESSING')
    amount = models.DecimalField('Сумма (в рублях)', max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField('Дата', auto_now_add=True)


class Payment(models.Model):
    """Entity for save info about successful withdrawal request."""

    withdrawal_request = models.OneToOneField(
        WithdrawalRequest,
        related_name='payment',
        on_delete=models.PROTECT,
        verbose_name='Запрос на вывод средств'
    )
