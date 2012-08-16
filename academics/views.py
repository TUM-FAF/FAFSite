from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


def addUserExtended(request):
    return render_to_response(
        "admin/academics/user/change_form.html",
        RequestContext(request, {}),
    )
UserExtended( = staff_member_required(addUserExtended)
