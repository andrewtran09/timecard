from .views import *
from django.urls import path


urlpatterns =[

    path('contract_rates/header/<int:pk>',contract_header,name='contract_header'),
    path('contract_rates/head_view', HeaderList.as_view(), name='head_list'),
    path('contract_rates/unit/<int:pk>', contract_unit, name='contract_unit'),
    path('contract_rates/unit_view',UnitList.as_view(),name='unit_list'),
    path('contract_rates/details/<int:pk>', contract_details, name='contract_details'),
    path('contract_rates/detail_view', DetailList.as_view(), name='detail_list'),
    path('contract_rates/transmit/<int:pk>', contract_transmit, name='contract_transmit'),
    path('contract_rates/trans_view', TransList.as_view(), name='trans_list'),

]
