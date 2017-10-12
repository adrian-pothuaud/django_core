import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from django_core_project.forms import ContactForm


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


def request_meta(request):
    return render(request, 'request_meta.html', context=None)


def simple_form_handling(request):
    return render(request, 'simple_form_handling.html', context=None)


def contact_form(request):
    form_get = ContactForm(
        initial={
            'subject': 'I love your site !',
            'email': 'noreply@{}.com'.format(
                request.get_host().replace(':', '')
            )
        }
    )
    form_post = ContactForm(
        initial={
            'subject': 'I love your site !',
            'email': 'noreply@{}.com'.format(
                request.get_host().replace(':', '')
            )
        }
    )
    if request.method == 'GET':
        if 'message' in request.GET.keys():
            # form have been sent
            form_get = ContactForm(request.GET)
            if form_get.is_bound and form_get.is_valid():
                if form_get.cleaned_data['email']:
                    send_mail(
                        form_get.cleaned_data['subject'],
                        "{}\n{}".format(form_get.cleaned_data['message'],
                                        form_get.cleaned_data['full_name']
                                        ),
                        form_get.cleaned_data['email'],
                        ['adrianpothuaud@gmail.com'],
                        fail_silently=False,
                    )
                else:
                    send_mail(
                        form_get.cleaned_data['subject'],
                        "{}\n{}".format(form_get.cleaned_data['message'],
                                        form_get.cleaned_data['full_name']
                                        ),
                        None,
                        ['adrianpothuaud@gmail.com'],
                        fail_silently=False,
                    )
    else:
        form_post = ContactForm(request.POST)
        if form_post.is_bound and form_post.is_valid():
            if form_post.cleaned_data['email']:
                send_mail(
                    form_post.cleaned_data['subject'],
                    "{}\n{}".format(form_post.cleaned_data['message'],
                                    form_post.cleaned_data['full_name']
                                    ),
                    form_post.cleaned_data['email'],
                    ['adrianpothuaud@gmail.com'],
                    fail_silently=False,
                )
            else:
                send_mail(
                    form_post.cleaned_data['subject'],
                    "{}\n{}".format(form_post.cleaned_data['message'],
                                    form_post.cleaned_data['full_name']
                                    ),
                    None,
                    ['adrianpothuaud@gmail.com'],
                    fail_silently=False,
                )
    return render(request, 'contact_form.html', context={
        'form_get': form_get,
        "form_post": form_post
    })
