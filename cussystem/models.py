from django.db import models
from django.utils import timezone 

# Create your models here.
# 报价表
# 订单表

# 每日客户
class WeekCus(models.Model):
	
	# 询盘时间 客户代码 客户名 国家 来源 邮箱 公司名称  网址 (客户类型-制造商/贸易商) 潜力  跟进平台 手机  跟进情况 最后跟进时间
	# 需要一个创建时间,和一个询盘时间 主要客户也是
	createtime = models.DateField(auto_now_add=True)
	inquirytime = models.DateField(default=timezone.now)
	cus_id = models.CharField(max_length=200, blank=True)
	cname = models.CharField(max_length=200, blank=True)
	ccountry = models.CharField(max_length=200, blank=True)
	cfrom = models.CharField(max_length=200, blank=True)
	cemail = models.CharField(max_length=200, blank=True)
	ccompany = models.CharField(max_length=200, blank=True)
	cwebsite = models.CharField(max_length=200, blank=True)
	ctype = models.CharField(max_length=200, blank=True)
	cgrade = models.CharField(max_length=200, blank=True)
	cplateform = models.CharField(max_length=200, blank=True)
	cphone = models.CharField(max_length=200, blank=True)
	# cqnumber = models.CharField(max_length=200, blank=True)

# 主要客户
class MainCus(models.Model):
	# 客户类型(ABCD放弃) 客户代码 客户名 国家 邮箱 询盘时间(创建),手机 报价数 订单数 最后跟进时间, 跟进详情
	cgrade = models.CharField(max_length=200, blank=True)
	inquirytime = models.DateField(default=timezone.now)
	cus_id = models.CharField(max_length=200, blank=True)
	cname = models.CharField(max_length=200, blank=True)
	ccountry = models.CharField(max_length=200, blank=True)
	cfrom = models.CharField(max_length=200, blank=True)
	cemail = models.CharField(max_length=200, blank=True)
	ccompany = models.CharField(max_length=200, blank=True)
	cwebsite = models.CharField(max_length=200, blank=True)
	ctype = models.CharField(max_length=200, blank=True)
	cplateform = models.CharField(max_length=200, blank=True)
	cphone = models.CharField(max_length=200, blank=True)
	cqnumber = models.CharField(max_length=200, blank=True)
	corders = models.CharField(max_length=200, blank=True)

# 报价时间
# 报价，设置为主要客户的外键
class Quotations(models.Model):
	customer = models.ForeignKey(MainCus, on_delete=models.CASCADE)
	quotetime = models.DateField(auto_now_add=True)
	part_name = models.CharField(max_length=200, blank=True)
	single_length = models.CharField(max_length=200, blank=True)
	single_width = models.CharField(max_length=200, blank=True)
	panel_length = models.CharField(max_length=200, blank=True)
	panel_width = models.CharField(max_length=200, blank=True)
	panel_size = models.CharField(max_length=200, blank=True)
	number_up = models.CharField(max_length=200, blank=True)
	average_size = models.CharField(max_length=200, blank=True)
	quantity = models.CharField(max_length=200, blank=True)
	amount_size = models.CharField(max_length=200, blank=True)
	basic_price = models.CharField(max_length=200, blank=True)
	RMB_price = models.CharField(max_length=200, blank=True)
	USD_price = models.CharField(max_length=200, blank=True)
	testing_fee = models.CharField(max_length=200, blank=True)
	amount = models.CharField(max_length=200, blank=True)
	material = models.CharField(max_length=200, blank=True)
	layer = models.CharField(max_length=200, blank=True)
	inner_copper = models.CharField(max_length=200, blank=True)
	finish_copper = models.CharField(max_length=200, blank=True)
	thickness = models.CharField(max_length=200, blank=True)
	solder = models.CharField(max_length=200, blank=True)
	silkscreen = models.CharField(max_length=200, blank=True)
	finish = models.CharField(max_length=200, blank=True)
	addings = models.CharField(max_length=200, blank=True)


# 订单时间
# 订单表，设置为主要客户的外键
class Orders(models.Model):
	customer = models.ForeignKey(MainCus, on_delete=models.CASCADE)
	ordertime = models.DateField(auto_now_add=True)
	single_length = models.CharField(max_length=200, blank=True)
	single_width = models.CharField(max_length=200, blank=True)
	panel_length = models.CharField(max_length=200, blank=True)
	panel_width = models.CharField(max_length=200, blank=True)
	panel_size = models.CharField(max_length=200, blank=True)
	number_up = models.CharField(max_length=200, blank=True)
	average_size = models.CharField(max_length=200, blank=True)
	quantity = models.CharField(max_length=200, blank=True)
	amount_size = models.CharField(max_length=200, blank=True)
	basic_price = models.CharField(max_length=200, blank=True)
	RMB_price = models.CharField(max_length=200, blank=True)
	USD_price = models.CharField(max_length=200, blank=True)
	testing_fee = models.CharField(max_length=200, blank=True)
	amount = models.CharField(max_length=200, blank=True)
	material = models.CharField(max_length=200, blank=True)
	layer = models.CharField(max_length=200, blank=True)
	inner_copper = models.CharField(max_length=200, blank=True)
	finish_copper = models.CharField(max_length=200, blank=True)
	thickness = models.CharField(max_length=200, blank=True)
	solder = models.CharField(max_length=200, blank=True)
	silkscreen = models.CharField(max_length=200, blank=True)
	finish = models.CharField(max_length=200, blank=True)
	addings = models.CharField(max_length=200, blank=True)

# 跟进 设置主要客户为外键
class Follows(models.Model):
	customer = models.ForeignKey(MainCus, on_delete=models.CASCADE)
	content_time = models.DateField(auto_now=True)
	content = models.TextField(blank=True)