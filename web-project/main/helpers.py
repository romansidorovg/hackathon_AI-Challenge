import joblib
import pandas as pd

from dataclasses import dataclass
from typing import Any
from django.core.files import File

from dbcore.models import InputFormModel, ResultModelFile
from main.forms import Form, InputFileForm 

@dataclass
class GetContext:

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        ctx = {
            'form': Form(),
            'file_form': InputFileForm(),
        }

        return ctx
    

@dataclass
class AIHelper:

    def predict(self, file):
        df = pd.read_csv(file)
        df = df.drop(columns='Unnamed: 0')
        model_file = InputFormModel.objects.last()
        model = joblib.load(f'media/{model_file.file}')

        try:
            result = model.predict(df)
        except:
            return False

        save_data = pd.DataFrame(columns=None, data=result)
        save_data.to_csv('file_to_save.csv', encoding='utf-8', index=True)

        return self._to_save()
    
    def _to_save(self):
        with open('file_to_save.csv', mode='rb') as f:
            return ResultModelFile.objects.create(file=File(f, name='file_to_save.csv'))


def best_composition(user_material, user_delivery_option, user_duration, user_amount, user_position_quantity):
    print(user_material, user_delivery_option, user_duration, user_amount, user_position_quantity)
    train = pd.read_csv('main/data/train_AIC(1).csv')
    train.rename(columns={'Вариант поставки' : 'Вариант_поставки', 'Количество позиций' : 'Количество_позиций'}, inplace=True)
    #из формы
    #user_material = 27439

    #из формы
    #user_delivery_option = 2

    #из формы
    #user_duration = 0
    #тут судя по всему user_duration = та дата, которую выбрал пользователь - текущая дата
    subtract_duration = user_duration - train['Длительность'].std()
    add_duration = user_duration + train['Длительность'].std()

    #хардкод позиций в js
    #формы
    #user_amount = 5.485452
    subtract_amount = user_amount - train['Сумма'].std()
    add_amount = user_amount + train['Сумма'].std()

    #Под вопросом пока
    #user_position_quantity = 1
    subtract_position_quantity = user_position_quantity - train['Количество_позиций'].std()
    add_position_quantity = user_position_quantity + train['Количество_позиций'].std()

    user_quantity = 1

    subtract_quantity = user_quantity - train['Количество'].std()
    add_quantity = user_quantity + train['Количество'].std()
    result = train.query(f"Материал == {user_material} \
                    and Вариант_поставки == {user_delivery_option}")\
        .groupby(['Поставщик', 'Категорийный менеджер', 'Операционный менеджер', 'Завод', 'Закупочная организация'], as_index=False)\
        .agg(mean_y=('y', 'mean'),count_y=('y', 'count')).sort_values(['mean_y', 'count_y'], ascending=[True, False])
    return result.loc[0, :]