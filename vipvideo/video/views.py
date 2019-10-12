from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from vipvideo.video.forms import UrlForm

video_api = [
    "https://www.administratorw.com/admin.php?url=",
    "https://yun.odflv.com/?url=",
    "http://goudidiao.com/?url=",
    "https://jx.maoyun.tv/index.php?id=",
    "http://www.1717yun.com/jx/vip/index.php?url=",
    "http://api.xfsub.com/index.php?url=",
    "http://q.z.vip.totv.72du.com/?url=",
    "http://jx.api.163ren.com/vod.php?url=",
    "http://www.0335haibo.com/tong.php?url=",
    "http://www.wmxz.wang/video.php?url=https://www.iqiyi.com/v_19rtplszi0.html",
    "http://www.vipjiexi.com/yun.php?url=",
    "https://hhh.qqplayer.cn/beac.php?url=",
    "http://j.zz22x.com/jx/?url=",
    "http://api.nepian.com/ckparse/?url=",
    "https://vip.bljiex.com/?v=",
    "http://vip.jlsprh.com/index.php?url=",
    'http://api.baiyug.vip/index.php?url=',
    'http://jiexi.071811.cc/jx2.php?url=',
    'http://app.baiyug.cn:2019/vip/?url=',
    'http://api.nepian.com/ckparse/?url=',
    'http://j.zz22x.com/jx/?url=',
    'http://api.wlzhan.com/sudu/?url=',
    "https://jiexi.071811.cc/jx.php?url=",
    "https://vip.mpos.ren/v/?url=",
    "http://jx.618g.com/?url=",
    "http://jx.cesms.cn/?url=",
    "https://660e.com/?url=",
    "https://api.sigujx.com/?url=",
    "https://www.ikukk.com/?url="
]


def index(request):
    form = UrlForm(request.POST)
    if request.method == 'POST':
        template = loader.get_template('video/result.html')
        res = []
        if form.is_valid():
            for a in video_api:
                res.append(a+form.cleaned_data.get("your_url"))
            context = {
                'url_list': res,
            }
            return HttpResponse(template.render(context, request))
        else:
            form = UrlForm()
    return render(request, 'video/video_home.html', {'form': form})


def parse_video(request, url):
    return HttpResponse("You're looking at question %s" % url)
