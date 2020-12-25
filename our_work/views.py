from django.shortcuts import render


def home(request):
    return render(request, "our_work/home.html")


def digital_singles(request):
    return render(request, "our_work/digital_singles.html")


def music_covers(request):
    return render(request, "our_work/music_covers.html")


def official_music_videos(request):
    return render(request, "our_work/official_music_videos.html")


def video_production(request):
    return render(request, "our_work/video_production.html")


def talent_management(request, person=None):
    if person is None:
        return render(request, "our_work/talent_management.html")
    else:
        return render(request, "our_work/talents/{}.html".format(person.replace("-", "_")))


def stage_performance(request):
    return render(request, "our_work/stage_performance.html")


def branded_content(request):
    return render(request, "our_work/branded_content.html")


def influencer_marketing(request):
    return render(request, "our_work/influencer_marketing.html")
