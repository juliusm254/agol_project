from django import views
from django.urls import path, include

# from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (LoginView, 
                    ScanOrder, 
                    # LabInspectionListCreateAPIView,
                    # SafetyCheckListCreateAPIView,
                    LabResultsVentListCreateAPIView,
                    LoadingListCreateAPIView,
                    OrderDetailView,
                    # LabResultsDetailView,
                    SafetyCheckListQuestionCreateAPIView,
                    # LabResultsListCreateAPIView,
                    # SafetyCheckListDetailAPIView
                    )

from .api import (
                    ChecklistCreateAPI, 
                    ChecklistListAPI, 
                    ChecklistDetailAPI, 
                    PrintSafetyListAPI, 
                    LabInspectionListAPI,
                    LabInspectionCreateAPI,
                    LabResultsCreateAPI,
                    LabResultsListAPI,
                    LabInspectionDetailsAPI,
                    LabSealListAPIView
                    )

# from accounts.views import UserCreate

# from .views import OrderViewSet, ScanOrderViewset



urlpatterns = [    
    
    path("login/", LoginView.as_view(), name="login"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_details"),
    path("scan-order/<int:pk>/", ScanOrder.as_view(), name="scan-order"),
    # path('checklist/', SafetyCheckListCreateAPIView.as_view(), name="check-list"),
    path('checklistcreate/', ChecklistCreateAPI.as_view(), name="check-list"),    
    path('checklist/', ChecklistListAPI.as_view(), name="check-list"),    
    path('checklist/<int:pk>/', ChecklistDetailAPI.as_view(), name="detail-checklist"),
    path('printsafety/', PrintSafetyListAPI.as_view(), name="safety-list"),
    
    # path('checklist/<int:pk>/', SafetyCheckListDetailAPIView.as_view(), name="detail-checklist"),
    path('checklist-questions/', SafetyCheckListQuestionCreateAPIView.as_view(), name="checklistquestions"),
    path('lab-inspection/', LabInspectionListAPI.as_view(), name="lab-inspection"),
    # path('lab-inspection/', LabInspectionListCreateAPIView.as_view(), name="lab-inspection"),
    path('lab-create/',LabInspectionCreateAPI.as_view(), name="lab-create"),
    # path('lab-details/',LabInspectionListCreateAPIView.as_view(), name="lab-details"),
    path('lab-results/',LabResultsListAPI.as_view(), name="lab-results"),
    path('lab-results-create/',LabResultsCreateAPI.as_view(), name="lab-results"),
    # path('lab-results/',LabResultsListCreateAPIView.as_view(), name="lab-results"),
    path('lab-results/<int:pk>/',LabInspectionDetailsAPI.as_view(), name="lab-results-details"),
    # path('lab-results/<int:pk>/',LabResultsDetailView.as_view(), name="lab-results-details"),
    path('lab-seal/',LabSealListAPIView.as_view(), name="lab-seal"),
    path('lab-vent/',LabResultsVentListCreateAPIView.as_view(), name="lab-results-details"),
    path('loading/',LoadingListCreateAPIView.as_view(), name="loading"),
    
    # path('lab-resultsdetails/',LabResultsListCreateAPIView.as_view(), name="lab-results-details"),
    
    # path('order-new/<int:pk>/',views.OrderUpdate.as_view()),
    
]