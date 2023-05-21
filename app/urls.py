from django.urls import path


from . import views

urlpatterns = [
    path('', views.TabataPageView.as_view(), name='home'),
    path('tabata/<slug:slug>', views.TrainingsDaysView.as_view(), name='train_detail'),
]