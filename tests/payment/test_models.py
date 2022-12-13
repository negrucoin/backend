import pytest

from payment.models import QIWIBill


@pytest.mark.django_db
@pytest.mark.parametrize('pk,excepted_hash',
                         [
                             (1, '2eb1aeef800554aab472e20a2592bd88'),
                             (2, '3deb01dd206f5374892c3d1bb1e9ac09'),
                             (3, 'd6dba0416958f7e8624b2523b7440610'),
                         ])
def test_generation_of_qiwi_bill_id(pk, excepted_hash, client):
    bill_id = QIWIBill.objects.get(pk=pk).bill_id
    assert bill_id == excepted_hash
