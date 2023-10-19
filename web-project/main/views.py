from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from django.http import FileResponse

from main.forms import Form, InputFileForm
from main.helpers import GetContext, AIHelper, best_composition


class MainView(View):
    def get(self, request):
        context = GetContext()()
        return render(request, 'index.html', context=context)
    

class GetFormData(View):
    def post(self, request):
        form = Form(request.POST)

        user_duration = datetime.strptime(form.data.get('user_duration'), '%Y-%m-%d').date() - datetime.now().date()
        result = best_composition(
            user_material=int(form.data.get('user_material')),
            user_delivery_option=int(form.data.get('user_delivery_option')),
            user_duration=user_duration.days,
            user_amount=float(form.data.get('user_quantity')),
            user_position_quantity=int(form.data.get('user_position_quantity')),
        )

        context = GetContext()()

        result_data = result.to_dict()
        result_data['Вероятность срыва'] = result_data.pop('mean_y')
        result_data['Срывов этой комбинации'] = result_data.pop('count_y')

        context['form_result'] = ', '.join([f'{k}: {v}' for k, v in result_data.items()])

        return render(request, 'index.html', context=context)
    

class AIView(View):
    def post(self, request, *args, **kwargs):
        form = InputFileForm(request.POST, request.FILES)

        if form.is_valid():
            res = AIHelper().predict(file=form.cleaned_data.get('file'))
            if res:
                return FileResponse(open(f'media/{res.file}', 'rb'))
            
        return redirect('main:main_page')
