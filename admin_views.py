from academics.models import UserMetaType
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


# def metakey(request):
#     return render_to_response(
#         "admin/books/report.html",
#         {'book_list' : Book.objects.all()},
#         RequestContext(request, {}),
#     )
# report = staff_member_required(report)


# def metakeys(request):
#     fieldset = ['aaaaaaaa', 'bbbbbbbbb', 'cccccccccc']
#     return render_to_response(
#         "admin/academics/user/change_form.html", 
#         RequestContext(request, {}))