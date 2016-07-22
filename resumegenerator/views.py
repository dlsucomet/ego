from django.shortcuts import render
from django.http import HttpResponse

#model imports
from models import Achievements
from models import Address
from models import Award
from models import Cellphone
from models import Curricular
from models import Education
from models import Login
from models import Researchpaper
from models import Seminarattend
from models import Seminarconduct
from models import Telephone
from models import User
from models import Workexp
#IMPORT Email
#IMPORT Objective
#IMPORT SchoolDescription
#IMPORT Background

# Create your views here.
def index(request):
	return render(request, 'resumegenerator/index.html')


def firstPage(request):
	return render(request, 'resumegenerator/DLSURGLogin.html')

def signUp(request):
	return render(request, 'resumegenerator/SignUp.html')

def mainPage(request):
	return render(request, 'resumegenerator/RGhomepage.html')

# def submitData(request):
	# if request.method == "POST":
		# userid = request.POST.get('userid')

		## achievements
		# achieveid = request.POST.get('achieveid')
		# achievement = request.POST.get('achievement')

		## address
		# addressid = request.POST.get('addressid')
		# address = request.POST.get('address')

		## award
		# awardid = request.POST.get('awardid')
		# award = request.POST.get('award')
		# yearaward = request.POST.get('yearaward')

		## cellphone
		# cellphoneid = request.POST.get('cellphoneid')
		# cellnum = request.POST.get('cellnum')

		## curricular
		# curricularid = request.POST.get('curricularid')
		# curricularyrstart = request.POST.get('curricularyrstart')
		# curricularyrfin = request.POST.get('curricularyrfin')
		# position = request.POST.get('position')
		# organization = request.POST.get('organization')
		# workdone = request.POST.get('workdone')

		## education
		# educationid = request.POST.get('educationid')
		# educationyrstart = request.POST.get('educationyrstart')
		# educationyrfin = request.POST.get('educationyrfin')
		# school = request.POST.get('school')
		# educattained = request.POST.get('educattained')
		# monthattained = request.POST.get('monthattained')
		# yearattained = request.POST.get('yearattained')

		## login
		# username = request.POST.get('username')
		# password = request.POST.get('password')

		## researchpaper
		# researchpaperid = request.POST.get('researchpaperid')
		# researchmonth = request.POST.get('researchmonth')
		# researchyear = request.POST.get('researchyear')
		# title = request.POST.get('title')
		# summary = request.POST.get('summary')

		## seminarattend
		# seminarattendid = request.POST.get('seminarattendid')
		# seminarattendmonth = request.POST.get('seminarattendmonth')
		# seminarattendyear = request.POST.get('seminarattendyear')
		# seminarattendtitle = request.POST.get('seminarattendtitle')
		# seminarattendhead = request.POST.get('seminarattendhead')
		# seminarattendvenue = request.POST.get('seminarattendvenue')


		## seminarconduct
		# seminarconductid = request.POST.get('seminarconductid')
		# seminarconductmonth = request.POST.get('seminarconductmonth')
		# seminarconductyear = request.POST.get('seminarconductyear')
		# seminarconductposition = request.POST.get('seminarconductposition')
		# seminarconducttitle = request.POST.get('seminarconducttitle')
		# seminarconducthead = request.POST.get('seminarconducthead')
		# seminarconductvenue = request.POST.get('seminarconductvenue')

		## telephone
		# telephoneid = request.POST.get('telephoneid')
		# telnum = request.POST.get('telnum')

		## user
		# firstname = request.POST.get('firstname')
		# middleinitial = request.POST.get('middleinitial')
		# lastname = request.POST.get('lastname')
		# email = request.POST.get('email')
		# objective = request.POST.get('objective')
		# background = request.POST.get('background')

		## workexp
		# workexpid = request.POST.get('workexpid')
		# monthstart = request.POST.get('monthstart')
		# yearstart = request.POST.get('yearstart')
		# monthfin = request.POST.get('monthfin')
		# yearfin = request.POST.get('yearfin')
		# position = request.POST.get('position')
		# company = request.POST.get('company')
		# workdone = request.POST.get('workdone')

		# achievements = Achievements(achieveid = achieveid, userid = userid, achievement = achievement)
		# address = Address(addressid = addressid, userid = userid, address = address)
		# award = Award(awardid = awardid, userid = userid, award = award, yearaward = yearaward)
		# cellphone = Cellphone(cellphoneid = cellphoneid, userid = userid, cellnum = cellnum)
		# curricular = Curricular(curricularid = curricularid, userid = userid, curricularyrstart = curricularyrstart, curricularyrfin = curricularyrfin, position = position, organization = organization, workdone = workdone)
		# education = Education(educationid = educationid, userid = userid, educationyrstart = educationyrstart, educationyrfin = educationyrfin, school = school, educattained = educattained, monthattained = monthattained, yearattained = yearattained)
		# login = Login(userid = userid, username = username, password = password)
		# researchpaper = Researchpaper(researchpaperid = researchpaperid, userid = userid, researchmonth = researchmonth, researchyear = researchyear, title = title, summary = summary)
		# seminarattend = Seminarattend(seminarattendid = seminarattendid, userid = userid, seminarattendmonth = seminarattendmonth, seminarattendyear = seminarattendyear, seminarattendtitle = seminarattendtitle, seminarattendhead = seminarattendhead, seminarattendvenue = seminarattendvenue)
		# seminarconduct = Seminarconduct(seminarconductid = seminarconductid, userid = userid, seminarconductmonth = seminarconductmonth, seminarconductyear = seminarconductyear, seminarconducthead = seminarconducthead, seminarconductposition = seminarconductposition, seminarconducttitle = seminarconducttitle, seminarconducthead = seminarconducthead, seminarconductvenue = seminarconductvenue)
		# telephone = Telephone(telephoneid = telephoneid, userid = userid, telnum = telnum)
		# user = User(userid = userid, firstname = firstname, middleinitial = middleinitial, lastname = lastname, email = email, objective = objective, background = background)
		# workexp = Workexp(workexpid = workexpid, userid = userid, monthstart = monthstart, yearstart = yearstart, monthfin = monthfin, yearfin = yearfin, position = position, company = company, workdone = workdone)

		# achievements.save()
		# address.save()
		# award.save()
		# cellphone.save()
		# curricular.save()
		# education.save()
		# login.save()
		# researchpaper.save()
		# seminarattend.save()
		# seminarconduct.save()
		# telephone.save()
		# user.save()
		# workexp.save()
	# return render(request, 'resumegenerator/index.html')
