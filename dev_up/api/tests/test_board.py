import json

from rest_framework.test import APITestCase

from api.tests.mock.board_posting_data import BoardPostingData
from api.tests.mock.category_mock import CategoryMock
from api.tests.mock.member_mock import MemberMock


class MeetingBoardTest(APITestCase, MemberMock, CategoryMock, BoardPostingData):

    def test_board_creating(self):
        member = self.create_member_mock()
        category = self.create_category_mock()

        data = json.dumps({
            'title': self.title,
            'contents': self.contents,
            'location': self.location,
            'meeting_capacity': self.meeting_capacity,
            'meeting_date': self.meeting_date,
            'meeting_times_of_day': self.meeting_times_of_day,
            'category_id': category.id,
            'author_name': member.id
        })

        result = self.client.post('/board/', data, content_type='application/json')

        self.assertEquals(result.status_code, 200)
        self.assertEquals(result.data['title'], self.title)
        self.assertEquals(result.data['contents'], self.contents)
        self.assertEquals(result.data['location'], self.location)
        self.assertEquals(result.data['meeting_capacity'], self.meeting_capacity)
        self.assertEquals(result.data['meeting_times_of_day'], self.meeting_times_of_day)
        self.assertEquals(result.data['author'], member.id)
        self.assertEquals(result.data['category'], category.id)
