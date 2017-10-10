import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context=None)


def hello_world(request):
    return render(request, 'hello_world.html', context=None)


def current_datetime(request):
    now = datetime.datetime.now()
    message = "It is now %s" % now
    return render(request, 'current_time.html', context={"now": now, "message": message})


def ahead_datetime(request, hours_ahead):
    now = datetime.datetime.now()
    ahead = now + datetime.timedelta(hours=int(hours_ahead))
    message = "It will be %s" % ahead
    return render(request, 'ahead_datetime.html', context={"now": now, "message": message})


def no_page(request):
    text = "No Page is set yet for this URL !"
    index_ref = "/"
    paragraph = "<p>{text}</p>"
    link = "<a href=\"{ref}\">{name}</a>"
    div = "<div>{content}</div>"
    html = "<html><head><link rel=\"shortcut icon\" type=\"image/png\" href=\"/static/images/favicon.ico\"/>" \
           "<title>No Page</title></head><body>{content}</body></html>"

    no_page_html = html.format(
        content="".join([
            div.format(
                content=paragraph.format(
                    text=text
                )
            ),
            div.format(
                content=link.format(
                    ref=index_ref,
                    name="Back"
                )
            )
        ])
    )

    return HttpResponse(no_page_html)


