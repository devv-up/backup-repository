from django.urls import path

from dev_up_api.services.meeting_board import MeetingBoard

urlpatterns = [
    path('board/', MeetingBoard.as_view(), name='board_create'),
]
