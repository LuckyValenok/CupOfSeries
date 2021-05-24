from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from friendship.views import (
    friendship_accept,
    friendship_cancel,
    friendship_reject,
    friendship_remove,
    FriendsView,
)

urlpatterns = [
    url(
        regex=r"^friends/$",
        view=login_required(FriendsView.as_view()),
        name="friendship_view_friends",
    ),
    url(
        regex=r"^friend/accept/(?P<friendship_request_id>\d+)/$",
        view=friendship_accept,
        name="friendship_accept",
    ),
    url(
        regex=r"^friend/reject/(?P<friendship_request_id>\d+)/$",
        view=friendship_reject,
        name="friendship_reject",
    ),
    url(
        regex=r"^friend/cancel/(?P<friendship_request_id>\d+)/$",
        view=friendship_cancel,
        name="friendship_cancel",
    ),
    url(
        regex=r"^friend/remove/(?P<username>[\w-]+)/$",
        view=friendship_remove,
        name="friendship_remove",
    )
]
