from django.db import IntegrityError

from .models import MyUser, Payment


async def create_user(t_name, t_username, t_user_id, username, email, password):
    try:
        return True, MyUser.objects.create_user(
            tele_name=t_name,
            tele_username=t_username,
            tele_user_id=t_user_id,
            username=username,
            email=email,
            password=password
        )
    except IntegrityError:
        return False, MyUser.objects.get(
            username=username,
        )


async def create_payment_info(t_user_id, t_name, t_username, payment_info):
    info = []
    for k, v in payment_info.items():
        info.append(f"{k} = {v}")
    obj = MyUser.objects.get(tele_user_id=t_user_id)
    if obj:
        obj.has_payment = True
        obj.payment = ' / '.join(info) + '\n\n'
        obj.save()


    try:
        return True, Payment.objects.create(
            user_id=t_user_id,
            name=t_name,
            username=t_username,
            payment_info=info
        )

    except IntegrityError:
        return False, Payment.objects.get(
            username=t_username,
        )
