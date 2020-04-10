from django.shortcuts import render
from .models import Banner, MiddleImage, Category, YogaBenefits, MoreYogaBenefits, AboutClasses, Testomonial, Features, AboutBlog, SubscribeDescription, Trainers, Contact, AboutUs, TrainerSectionHeading, OurInformation, ClassType, PostComment, ClassDetails, BlogSingle
from django.views.generic import TemplateView, CreateView
from django.template.context import RequestContext
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['banner_heading'] = Banner.objects.last()
        context['banner_video'] = Banner.objects.last()
        context['middle_image'] = MiddleImage.objects.last()
        context['category'] = Category.objects.all()
        context['yoga_benefits'] = YogaBenefits.objects.last()
        context['more_yoga_benefits'] = MoreYogaBenefits.objects.last()
        context['about_classes'] = AboutClasses.objects.last()
        context['class_details'] = ClassDetails.objects.all()
        context['testomonial'] = Testomonial.objects.all()
        context['features'] = Features.objects.all()
        context['blog_single'] = BlogSingle.objects.all()
        context['blog'] = AboutBlog.objects.last()
        
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['features'] = Features.objects.all()
        context['trainer_detail'] = TrainerSectionHeading.objects.last()
        context['trainer'] = Trainers.objects.all()
        context['about_us'] = AboutUs.objects.all()
        return context

class ClassesView(TemplateView):
    template_name = 'classes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClassesView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['class_details'] = ClassDetails.objects.all()
        context['trainer_detail'] = TrainersSectionHeading.objects.last()
        context['trainer'] = Trainers.objects.all()
        return context


class ClassesTypeView(TemplateView):
    template_name = 'classes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClassesTypeView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['class_details'] = ClassDetails.objects.filter(type_id=kwargs.get('pk'))
        context['trainer_detail'] = TrainerSectionHeading.objects.last()
        context['trainer'] = Trainers.objects.all()
        return context

class ClassSingleView(TemplateView):
    template_name = 'classSingle.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ClassSingleView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['class_details'] = ClassDetails.objects.get(id=kwargs.get('pk'))
        context['trainer'] = Trainers.objects.all()
        context['trainer_detail'] = TrainerSectionHeading.objects.last()
        return context


class SingleView(TemplateView):
    template_name = 'single.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SingleView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        blog_single = BlogSingle.objects.get(id=kwargs.get('pk'))
        blog_single.views += 1
        blog_single.save()
        context['blog_single'] = blog_single
        context['comments'] = PostComment.objects.filter(blog_id=kwargs.get('pk'))
        context['popular'] = BlogSingle.objects.filter(views__gte=1)
        return context
    
def commentview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("description")
        blog = BlogSingle.objects.get(pk=kwargs.get('pk'))
        PostComment.objects.create(name=name, email=email, description=description, blog=blog)

        return HttpResponseRedirect('/single/'+ str(kwargs.get('pk')))
    else:
        banner_image = Banner.objects.last()
        return render(request,'single.html',{'banner_image':banner_image})



class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['blog_single'] = BlogSingle.objects.all()
        
        return context

def contactview(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        description = request.POST.get("description")

        Contact.objects.create(name=name, email=email, phone=phone, description=description)

        return HttpResponseRedirect('/')
    else:
        banner_image = Banner.objects.last()
        testimonial = Testomonial.objects.all()
        our_information = OurInformation.objects.last()
        return render(request, 'contact.html', {'banner_image': banner_image, 'testomonial': testimonial, 'our_information': our_information})        

    

def index(request):
    return render(request, "index.html")


def subscribe(request, *args, **kwargs):
    if request.method == 'POST':
        if request.POST.get('subscribe'):
            email = request.POST.get('email')
            Subscribe.objects.create(email=email)
        return HttpResponseRedirect('/')


def search(request, *args, **kwargs):
    key=request.GET.get('search')
    classes = ClassDetails.objects.filter(Q(heading__icontains=key)|Q(type__name=key))
    return render(request, 'search.html', {'class_details': classes})

class ContentView(TemplateView):
    template_name = 'content.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ContentView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['category'] = Category.objects.get(id=kwargs.get('pk'))
        
        return context


class YogaBenefitsView(TemplateView):
    template_name = 'yogaBenefits.html'

    def get_context_data(self, *args, **kwargs):
        context = super(YogaBenefitsView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['yoga_benefits'] = YogaBenefits.objects.last()

        return context


class MoreYogaView(TemplateView):
    template_name = 'moreYoga.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MoreYogaView,self).get_context_data(**kwargs)
        context['banner_image'] = Banner.objects.last()
        context['more_yoga_benefits'] = MoreYogaBenefits.objects.last()

        return context