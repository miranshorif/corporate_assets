from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    # path('assign/<int:asset_id>/', views.assign_asset, name='assign_asset'),
    # path('return/<int:asset_id>/', views.return_asset, name='return_asset'),
    
    path('company/<int:company_id>/', views.company_dashboard, name='company_dashboard'),
    path('company/<int:company_id>/add/', views.add_employee, name='add_employee'),
    path('company/<int:company_id>/update/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('company/<int:company_id>/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    
    
    path('company/<int:company_id>/delegate/', views.delegate_device, name='delegate_device'),
    path('company/<int:company_id>/undelegate/<int:delegation_id>/', views.undelegate_device, name='undelegate_device'),
    path('device/<int:device_id>/history/', views.device_history, name='device_history'),
]
