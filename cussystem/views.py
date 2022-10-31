from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from .models import WeekCus, MainCus, Orders, Quotations, Follows
from django.views import generic
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime as dt
# Create your views here.
# 不理想的客户放弃掉
# 理想的客户加入主要客户表
# 先增删改查


# 每日客户展示
class IndexView(generic.ListView):
	template_name = 'cussystem/index.html'
	context_object_name = 'weekcus'

	def get_queryset(self):
		return WeekCus.objects.all().order_by("cus_id")



# 主要客户展示
class MaincView(generic.ListView):
	template_name = 'cussystem/maincus.html'
	context_object_name = 'maincus'

	def get_queryset(self):
		return MainCus.objects.all().order_by("cus_id")


# 展示所有询盘
class QuotationsView(generic.ListView):
	template_name = 'cussystem/quotations.html'
	context_object_name = 'quotations'

	def get_queryset(self):
		return Quotations.objects.all()

# 添加每日客户
def addwc(request):
	# addingwc = WeekCus(cus_id=request.POST.get("cus_id"), cname=POST.get("cname"),ccountry=request.POST.get("ccountry"), cfrom=POST.get("cfrom"),cemail=request.POST.get("cemail"), ccompany=POST.get("ccompany"),cwebsite=request.POST.get("cwebsite"), ctype=POST.get("ctype"),cgrade=request.POST.get("cgrade"), cplateform=POST.get("cplateform"),cphone=POST.get("cphone"))
	cus_id = request.POST.get("cus_id").replace(" ", "")
	cname = request.POST.get("cname")
	ccountry = request.POST.get("ccountry")
	cfrom = request.POST.get("cfrom")
	cemail = request.POST.get("cemail")
	ccompany = request.POST.get("ccompany")
	cwebsite = request.POST.get("cwebsite")
	ctype = request.POST.get("ctype")
	cgrade = request.POST.get("cgrade")
	cplateform = request.POST.get("cplateform")
	cphone = request.POST.get("cphone")
	cus_ids = []
	for weekcus in WeekCus.objects.all():
		cus_ids.append(weekcus.cus_id)
	if cus_id:
		if not cus_id  in cus_ids:
			addingwc = WeekCus(cus_id=cus_id, cname=cname, ccountry=ccountry, cfrom=cfrom, cemail=cemail, ccompany=ccompany, cwebsite=cwebsite, ctype=ctype, cgrade=cgrade, cplateform=cplateform, cphone=cphone)
			addingwc.save()
			return redirect('cussystem:index')
		return redirect('cussystem:index')
	else:
		return redirect('cussystem:index', )

#删除每日客户
def deleteswc(request):
	cus_id = request.POST.get("cus_id").replace(" ", "")

	if cus_id:
		weekcus = WeekCus.objects.get(cus_id=cus_id)
		weekcus.delete()
		return redirect("cussystem:index")
	else:
		message="没得到"
		return render(request, "cussystem/index.html", {"weekcus": WeekCus.objects.all(), "message":message})

# 编辑每日客户
def editwc(request):
	cus_id1 = request.POST.get("cus_id1").replace(" ", "")
	cus_id2 = request.POST.get("cus_id2").replace(" ", "")
	cname = request.POST.get("cname")
	cinquirytime = request.POST.get("cinquirytime")
	cinquirytime = cinquirytime.replace("年","-").replace("月","-").replace("日","")
	ccountry = request.POST.get("ccountry")
	cfrom = request.POST.get("cfrom")
	cemail = request.POST.get("cemail")
	ccompany = request.POST.get("ccompany")
	cwebsite = request.POST.get("cwebsite")
	ctype = request.POST.get("ctype")
	cgrade = request.POST.get("cgrade")
	cplateform = request.POST.get("cplateform")
	cphone = request.POST.get("cphone")

	weekcus = WeekCus.objects.get(cus_id=cus_id1)

	weekcus.cname = cname
	weekcus.ccountry = ccountry
	weekcus.inquirytime = cinquirytime
	weekcus.cfrom = cfrom
	weekcus.cemail = cemail
	weekcus.ccompany = ccompany
	weekcus.cwebsite = cwebsite
	weekcus.ctype = ctype
	weekcus.cgrade = cgrade
	weekcus.cplateform = cplateform
	weekcus.cphone = cphone
	weekcus.save()

	maincus = get_object_or_404(MainCus, cus_id=cus_id1)
	if maincus:
		maincus.inquirytime = cinquirytime
		maincus.cname = cname
		maincus.ccountry = ccountry
		maincus.cfrom = cfrom
		maincus.cemail = cemail
		maincus.ccompany = ccompany
		maincus.cwebsite = cwebsite
		maincus.ctype = ctype
		maincus.cgrade = cgrade
		maincus.cplateform = cplateform
		maincus.cphone = cphone
		maincus.save()
		return redirect("cussystem:index")
	else:
		return redirect("cussystem:index")





# 每周客户添加到主要客户
@csrf_exempt
def addtomainc(request):
	main_ids = []	
	mainc = MainCus.objects.all()

	for mid in mainc:
		main_ids.append(mid.cus_id)

	if request.is_ajax():
		if request.method == 'POST':
			msg = "发送成功,并且是post"
			ids = json.loads(request.body.decode('utf-8'))
			cus_ids = ids.get("ids")
			if len(cus_ids) >0:
				addedcusids = []
				addsuccess = []
				for cus_id in cus_ids:
					if not cus_id in main_ids:
						wc = WeekCus.objects.get(cus_id=cus_id)
						cname = wc.cname
						ccountry = wc.ccountry
						cemail = wc.cemail
						cfrom = wc.cfrom
						ccompany = wc.ccompany
						cwebsite = wc.cwebsite
						ctype = wc.ctype
						cgrade = wc.cgrade
						cplateform = wc.cplateform
						cphone = wc.cphone
						inquirytime = wc.inquirytime

						a = MainCus(cus_id=cus_id, cname=cname, ccountry=ccountry, cemail=cemail, cfrom=cfrom, ccompany=ccompany, cwebsite=cwebsite, ctype=ctype, cgrade=cgrade,cplateform=cplateform, cphone=cphone, inquirytime=inquirytime)
						a.save()
						addsuccess.append(cus_id)
						
					else:
						addedcusids.append(cus_id)
				return JsonResponse({"msg":"添加成功","addedcusids":addedcusids, "addsuccess":addsuccess})
			else:
				return JsonResponse({"msg":"添加失败: 请选择要加入的客户"})
	else:
		msg = "没成功"
		return JsonResponse({"cus_id":cus_id, "msg":msg})


#删除主要客户
def deletemcs(request):
	cus_id = request.POST.get("cus_id")

	if cus_id:
		maincus = MainCus.objects.get(cus_id=cus_id)
		maincus.delete()
		return redirect("cussystem:maincus")
	else:
		message="删除失败"
		return render(request, "cussystem/index.html", {"weekcus": WeekCus.objects.all(), "msg":message})

# 增加报价
def addquote(request):
	cus_id = request.POST.get("cus_id_quote").replace(" ", "")
	single_length = request.POST.get("single_length")
	panel_length = request.POST.get("panel_length")
	number_up = request.POST.get("number_up")
	basic_price = request.POST.get("basic_price")
	testing_fee = request.POST.get("testing_fee")
	material = request.POST.get("material")
	layer = request.POST.get("layer")
	inner_copper = request.POST.get("inner_copper")
	thickness = request.POST.get("thickness")
	solder = request.POST.get("solder")
	quantity = request.POST.get("quantity")
	single_width = request.POST.get("single_width")
	panel_width = request.POST.get("panel_width")
	panel_size = request.POST.get("panel_size")
	average_size = request.POST.get("average_size")
	amount_size = request.POST.get("amount_size")
	RMB_price = request.POST.get("RMB_price")
	USD_price = request.POST.get("USD_price")
	amount = request.POST.get("amount")
	finish_copper = request.POST.get("finish_copper")
	silkscreen = request.POST.get("silkscreen")
	finish = request.POST.get("finish")
	part_name = request.POST.get("part_name")
	addings = request.POST.get("addings")

	maincus = MainCus.objects.get(cus_id=cus_id)
	q = maincus.quotations_set.create()
	q.single_length = single_length
	q.panel_length = panel_length
	q.number_up = number_up
	q.basic_price = basic_price
	q.testing_fee = testing_fee
	q.material = material
	q.layer = layer
	q.thickness = thickness
	q.solder = solder
	q.quantity = quantity
	q.single_width = single_width
	q.panel_width = panel_width
	q.panel_size = panel_size
	q.average_size = average_size
	q.amount_size = amount_size
	q.RMB_price = RMB_price
	q.USD_price = USD_price
	q.amount = amount
	q.finish_copper = finish_copper
	q.silkscreen = silkscreen
	q.finish = finish
	q.part_name = part_name
	q.addings = addings

	q.save()
	return render(request, "cussystem/maincus.html", {"maincus":MainCus.objects.all()})


def orders(request):
	pass

@csrf_exempt
def get_quotes(request):
	cus_ids = json.loads(request.body.decode('utf-8'))
	cus_id = cus_ids.get("cus_id")

	maincus = MainCus.objects.get(cus_id=cus_id)
	quotes = maincus.quotations_set.all()

	return render(request, "cussystem:maincus", {"quotes":quotes, "maincus": MainCus.objects.all()})
	# return JsonResponse({"part_name":part_name})