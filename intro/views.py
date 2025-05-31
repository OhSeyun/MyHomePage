from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import GuestbookMessage


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        if name and message:
            msg = GuestbookMessage.objects.create(name=name, message=message)

            if "my_messages" not in request.session:
                request.session["my_messages"] = []
            request.session["my_messages"].append(msg.id)
            request.session.modified = True

            return redirect("/")

    messages = GuestbookMessage.objects.order_by("-created_at")
    my_ids = request.session.get("my_messages", [])
    return render(request, "intro/home.html", {
        "messages": messages,
        "my_ids": my_ids
    })


@require_POST
def delete_message(request, msg_id):
    my_ids = request.session.get("my_messages", [])
    if msg_id in my_ids:
        GuestbookMessage.objects.filter(id=msg_id).delete()
    return redirect("/")
