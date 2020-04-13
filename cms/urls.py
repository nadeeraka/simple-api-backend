from django.urls import include, path
from rest_framework import routers
from cms import views
###
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'income', views.IncomeViewSet)
router.register(r'incomeType', views.IncomeTypeViewSet)
router.register(r'expense', views.ExpenseViewSet)
router.register(r'saving', views.SavingViewSet)
router.register(r'savingType', views.SavingTypeViewSet)
router.register(r'balance', views.BalanceViewSet)
router.register(r'expenseType', views.ExpenseTypeViewSet)
router.register(r'account', views.reg_view, basename='reg')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
1