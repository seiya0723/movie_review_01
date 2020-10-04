from django.shortcuts import render

# Create your views here.
from django.views import View

class HomeView(View):

    def get(self, request, *args, **kwargs):

        """
        if "id" in request.GET:
            data    = モデルのクラス名.objects.filter(id=request.GET["id"])
            context = {"data":data}

            return render(request,"動画個別ページのテンプレート",context)
            
        if "category" in request.GET:
            data    = モデルのクラス名.objects.filter(category=request.GET["category"])
            context = {"data":data}

            return render(request,"カテゴリ別ページのテンプレート",context)

        """


        return render(request,"home/index.html")


    def post(self, request, *args, **kwargs):

        pass

index   = HomeView.as_view()
