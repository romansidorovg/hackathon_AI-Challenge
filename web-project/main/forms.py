from django import forms


class Form(forms.Form):
    user_material = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                    'value':"${productInputName.value}",
                                    'type':"text",
                                    'name':"cart_product_name_${productsCount}",
                                    'id':"cart_product_name_${productsCount}",
                                    'class':"tab-content-input tab-content-input_cart tab-content-input_cart-product-name",}),
                                )
    user_amount = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                'value':"${productInputCount.value}",
                                'type':"text",
                                'name':"cart_product_count_${productsCount}",
                                'id':"cart_product_count_${productsCount}",
                                'class':"tab-content-input tab-content-input_cart tab-content-input_cart-product-count",})
                                )
    user_duration = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                'value':"${productInputDate.value}",
                                'type':"text",
                                'name':"cart_product_delivery-date_${productsCount}",
                                'id':"cart_product_delivery-date_${productsCount}",
                                'class':"tab-content-input tab-content-input_cart tab-content-input_cart-delivery-date",})
                                )
    user_delivery_option = forms.CharField(required=False,
                            widget=forms.TextInput(attrs={
                            'value':"${productInputDeliveryVer.value}",
                            'type':"text",
                            'name':"cart_product_delivery-ver_${productsCount}",
                            'id':"cart_product_delivery-ver_${productsCount}",
                            'class':"tab-content-input tab-content-input_cart tab-content-input_cart-delivery-ver",})
                                )
    amount = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                'value':"${productInputPrice.value}",
                                'type':"text",
                                'name':"cart_product-price_${productsCount}",
                                'id':"cart_product-price_${productsCount}",
                                'class':"tab-content-input tab-content-input_cart tab-content-input_cart-product-price",})
                                )
    user_position_quantity = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                'placeholder':"Кол-во позиций",
                                'type':"number",
                                'value':"0",
                                'name':"cart_count_total",
                                'id':"cart_count_total",
                                'class':"tab-content-input tab-content-input_cart-total tab-content-input_cart-count-total",})
                                )
    user_quantity = forms.CharField(required=False,
                                widget=forms.TextInput(attrs={
                                'placeholder':"Сумма позиций",
                                'type':"number",
                                'value':"0",
                                'name':"cart_pirce_total",
                                'id':"cart_pirce_total",
                                'class':"tab-content-input tab-content-input_cart-total tab-content-input_cart-pirce-total",})
                                )
    

class InputFileForm(forms.Form):
    file = forms.FileField()