from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign


def dashboard(request):
    return render(request, "dashboard.html")


def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, "campaign_list.html", {"campaigns": campaigns})


def campaign_create(request):
    if request.method == "POST":
        Campaign.objects.create(
            name=request.POST.get("name"),
            platform=request.POST.get("platform"),
            budget=request.POST.get("budget"),
            start_date=request.POST.get("start_date"),
            end_date=request.POST.get("end_date"),
            status=request.POST.get("status"),
            city=request.POST.get("city"),
        )
        return redirect("/campaigns/")
    return render(request, "campaign_form.html", {"title": "Create Campaign"})


def campaign_edit(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    if request.method == "POST":
        for field, value in request.POST.items():
            if field != "csrfmiddlewaretoken":
                setattr(campaign, field, value)
        campaign.save()
        return redirect("/campaigns/")
    return render(request, "campaign_form.html", {
        "title": "Edit Campaign",
        "campaign": campaign
    })


def campaign_delete(request, id):
    Campaign.objects.filter(id=id).delete()
    return redirect("/campaigns/")
