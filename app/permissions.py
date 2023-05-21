from django.http import Http404


class PaymentPermissionsMixin:
    def has_permissions(self):
        if self.request.user.is_superuser:
            return True
        elif self.request.user.has_payment == True:
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)
