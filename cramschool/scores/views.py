from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from scores.forms import ScoresForm
from scores.models import Scores
from main.views import paginating, admin_required


def scores(request):
    scoress = paginating(request, Scores.objects.all())
    return render(request, 'scores/scores.html', {'scoress':scoress})

@admin_required
def scoresCreate(request):
    template = 'scores/scoresCreate.html'
    if request.method=='GET':
        return render(request, template, {'form':ScoresForm()})
    form = ScoresForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, template, {'form':form})
    scores = form.save()
    scores.save()   
    messages.success(request, '師資資料已新增') 
    return redirect(reverse('scores:scores'))


def scoresSearch(request):
    searchTerm = request.GET.get('searchTerm')
    scoress = paginating(request, Scores.objects.filter(Q(sid__icontains=searchTerm) |Q(tid__icontains=searchTerm) |Q(cid__icontains=searchTerm) |Q(scid__icontains=searchTerm) | Q(score__icontains=searchTerm)))
    return render(request, 'scores/scores.html', {'scoress':scoress})


@admin_required
def scoresDelete(request, scoresID):
    if request.method=='GET':
        return scores(request)
    # POST
    scores = get_object_or_404(Scores, scid=scoresID)
    scores.delete()
    messages.success(request, '師資資料已刪除')
    return redirect('scores:scores')

@admin_required
def scoresUpdate(request, scoresID):
    template = 'scores/scoresUpdate.html'
    scoresToUpdate = get_object_or_404(Scores, scid=scoresID)
    if request.method=='GET':            
        form = ScoresForm(instance=scoresToUpdate)
        return render(request, template, {'form':form, 'scores':scoresToUpdate})
    # POST
    form = ScoresForm(request.POST, instance=scoresToUpdate)
    if not form.is_valid():
        return render(request, template, {'form':form, 'scores':scoresToUpdate})
    scores=form.save()
    messages.success(request, '師資資料已修改')
    return redirect('scores:scores')