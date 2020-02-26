import json

from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.board_serializers import BoardSerializer
from api.models import Board, Category, Member


class MeetingBoard(APIView):
    def post(self, request):
        request_body = json.loads(request.body.decode('utf-8'))

        board = Board.objects.create(
            title=request_body.get('title'),
            contents=request_body.get('contents'),
            location=request_body.get('location'),
            meeting_capacity=request_body.get('meeting_capacity'),
            meeting_date=request_body.get('meeting_date'),
            meeting_times_of_day=request_body.get('meeting_times_of_day'),
            category=Category.objects.get(pk=request_body.get('category_id')),
            author=Member.objects.get(id=request_body.get('id'))
        )

        return Response(BoardSerializer(board).data)
