import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import Item, Order
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateChecoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[
                {
                    'price_data':{
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name':item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id":item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN+'/success/',
            cancel_url=YOUR_DOMAIN+ f'/item/{item.id}/',
        )
        return JsonResponse({
            'id':checkout_session.id
        })

class SuccessView(TemplateView):
    template_name='success.html'

class CancelView(TemplateView):
    template_name='cancel.html'

class ProductsLandingView(TemplateView):
    template_name='landing.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        product = Item.objects.get(id=item_id)
        context = super(ProductsLandingView, self).get_context_data(**kwargs)
        context.update({
            "product":product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context
