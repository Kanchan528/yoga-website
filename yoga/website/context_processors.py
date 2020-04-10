from .models import SubscribeDescription, OurInformation, ClassType

def footer_context(request, *args, **kwargs):
    subscribe_description = SubscribeDescription.objects.last()
    our_information = OurInformation.objects.last()
    classtype = ClassType.objects.all()   
    context = {'subscribe_description':subscribe_description, 'our_information':our_information, 'classtype':classtype}
    return context
