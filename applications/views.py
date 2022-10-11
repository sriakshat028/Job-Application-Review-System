from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Candidate,Education,Experience,Skills
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    candidates=Candidate.objects.all()
    context={'candidates':candidates}
    return render(request,'applications/index.html',context)

def description(request,candidate_id):
    candidate=Candidate.objects.get(id=candidate_id)
    if request.method == "POST":
        accepted=request.POST.get('accept',False)
        rejected=request.POST.get('reject', False)
        if accepted:
            candidate.status="Accepted"
        elif rejected:
            candidate.status="Rejected"
        candidate.save()
        return HttpResponseRedirect(reverse('index'))
    
    context={'candidate':candidate}
    return render(request,'applications/description.html',context)

def create(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['phone']
        gender=request.POST['gender']
        address=request.POST['address']
        country=request.POST['Country']
        state=request.POSt['State']
        city=request.POSt['City']
        postal_code=request.POST['Zip']
        role=request.POST['role']
        email=request.POST['email']
        resume=request.FILES['resume']
        fs=FileSystemStorage()
        fs.save(resume.name,resume)

        new_candidate = Candidate(
            first_name=first_name,
            last_name=last_name,
            address=address,
            country=country,
            state=state,
            city=city,
            postal_code=postal_code,
            phone=phone,
            gender=gender,
            email=email,
            role=role
        )
        new_candidate.save()
        count=1
        while True:
            try:
                institute=request.POST['institute'+(str)(count)]
                degree=request.POST['degree'+(str)(count)]
                course=request.POST['course'+(str)(count)]
                start_date=request.POST['start_date'+(str)(count)]
                end_date=request.POST['end_date'+(str)(count)]
                education=Education(
                    candidate=Candidate.objects.get(pk=new_candidate.id),
                    institute=institute,
                    degree=degree,
                    course=course,
                    start_date=start_date,
                    end_date=end_date
                )
                education.save()
            except  MultiValueDictKeyError:
                break
            count+=1
        
        count=1
        while True:
            try:
                company=request.POST['company'+(str)(count)]
                role=request.POST['role'+(str)(count)]
                start_date=request.POST['start_date'+(str)(count)]
                end_date=request.POST['end_date'+(str)(count)]
                responsibilities=request.POST['responsibilities'+(str)(count)]
                experience=Experience(
                    candidate=Candidate.objects.get(pk=new_candidate.id),
                    company=company,
                    role=role,
                    start_date=start_date,
                    end_date=end_date,
                    responsibilities=responsibilities
                )
                experience.save()
            except MultiValueDictKeyError:
                break
            count+=1
        
        count=1
        while True:
            try:
                skill=Skills(
                    candidate=Candidate.objects.get(pk=new_candidate.id),
                    skill=request.POST['skill'+(str)(count)]
                )
                skill.save()
            except MultiValueDictKeyError:
                break
            count+=1
        return HttpResponseRedirect(reverse('index'))
    return render(request,'applications/create.html')

