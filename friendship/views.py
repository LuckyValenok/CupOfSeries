from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import FriendForm
from .models import Friend

try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User


class FriendsView(View):
    def get(self, request):
        """ View the friends of a user """
        user = get_object_or_404(user_model, username=request.user.username)
        friends = Friend.objects.friends(user)
        requests = Friend.objects.requests(user)
        send_requests = Friend.objects.sent_requests(user)
        return render(
            request,
            'friendship/friend/user_list.html',
            {
                "friends": friends,
                "requests": requests,
                "send_requests": send_requests,
                "form": FriendForm()
            },
        )

    def post(self, request):
        form = FriendForm(data=request.POST)
        if form.is_valid():
            to_user = user_model.objects.get(username=form.cleaned_data['username'])
            from_user = request.user
            Friend.objects.add_friend(from_user, to_user)
        return redirect('friendship_view_friends')


@login_required
def friendship_accept(request, friendship_request_id):
    """ Accept a friendship request """
    f_request = get_object_or_404(
        request.user.friendship_requests_received, id=friendship_request_id
    )
    f_request.accept()
    return redirect("friendship_view_friends")


@login_required
def friendship_reject(request, friendship_request_id):
    """ Reject a friendship request """
    f_request = get_object_or_404(
        request.user.friendship_requests_received, id=friendship_request_id
    )
    f_request.reject()
    return redirect("friendship_view_friends")


@login_required
def friendship_cancel(request, friendship_request_id):
    """ Cancel a previously created friendship_request_id """
    f_request = get_object_or_404(
        request.user.friendship_requests_sent, id=friendship_request_id
    )
    f_request.cancel()
    return redirect("friendship_view_friends")


@login_required
def friendship_remove(request, username):
    to_user = user_model.objects.get(username=username)
    from_user = request.user
    Friend.objects.remove_friend(from_user, to_user)
    return redirect('friendship_view_friends')
