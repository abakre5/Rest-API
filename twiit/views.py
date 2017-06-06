from django.shortcuts import render
import twitter
import os
from project.twiit.models import Document


# Create your views here.
def index(request):
    api = twitter.Api(consumer_key = 'oKicPygcqTsWqh7O6PTWsKVoM',
                      consumer_secret='bfx0wMmaoKEfoEcAt3ZjrI6QKGPSSFefk8ERTgHkxykbjTPcsd',
                      access_token_key='842787620627341313-0Lnf0sRaB1qHt200cUnxNTwUC6RV31d',
                      access_token_secret='HU8aD8DTc2ec7aoWYauOekPxR6huRivcEYAB6OadeSTVI')

    is_file = request.FILES.get('docfile', False)
    if request.method == 'POST' and is_file and request.FILES['docfile'].name != '':
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            api.PostMedia(request.POST['texttweet'], 'media\/'+ request.FILES['docfile'].name)
            os.remove('media\/'+ request.FILES['docfile'].name)
    elif request.method == 'POST':
        stat = request.POST['texttweet']
        x = api.PostUpdate(stat)

    statuses = api.GetHomeTimeline(count=50)
    return render(request,
        'index.html' ,
        { 'statuses' : statuses}
    )

