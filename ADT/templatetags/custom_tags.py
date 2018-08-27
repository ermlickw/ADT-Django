from django import template
register = template.Library()
import numpy as np
from ..models import Claim


def get_all_children(self):
    children = []
    written = [self.number]
    appNumber = self.appNumber
    totalclaims =Claim.objects.filter(appNumber=appNumber).values_list('number', flat=True)
    listofchildren = []
    child_list = self.childs.all().order_by('number')
    terminate = False
    i=0

#need the query to be at start of loop to avoid cache errors
    while terminate == False:

        child = child_list[i]
        print(child)
        print(child.childs.all())
        listofchildren = child_list.values_list('number', flat=True)
        ### if the child has yet to be written:
        if child.number not in written:
            children.append(child.number)
            written.append(child.number)
            # print(children)
            # print(len(np.setdiff1d(listofchildren, written)))
        if child_list[i+1]:
            i+=1
        if (child.childs.all() != None and
            len(np.setdiff1d(listofchildren, written)) > 0):   #and we still have some children to write
            # print(np.setdiff1d(written,listofchildren))ddsc
            child_list = child.childs.all().exclude(number__in=np.setdiff1d(written,listofchildren)) #minus the already written claims
            i=0
            print(child_list)
            # print(np.setdiff1d(written,listofchildren))
        else:
            child_list = child.parent.childs.all() #go up a level and get the child list again
            i=0

        if len(np.setdiff1d(totalclaims, children)) > 0:
            terminate = True


    return children
#needs to be a while loop.. this doesnt work
    # for child in child_list:
    #     print(child)
    #     print(child.childs.all())
    #     listofchildren = child_list.values_list('number', flat=True)
    #     ### if the child has yet to be written:
    #     if child.number not in written:
    #         children.append(child.number)
    #         written.append(child.number)
    #         print(children)
    #         print(len(np.setdiff1d(listofchildren, written)))
    #         print(child.childs.all())
    #     if (child.childs.all() != None and
    #         len(np.setdiff1d(listofchildren, written)) > 0):   #and we still have some children to write
    #         # print(np.setdiff1d(written,listofchildren))
    #         child_list = child.childs.all().exclude(number__in=np.setdiff1d(written,listofchildren)) #minus the already written claims
    #         print(child_list)
    #     else:
    #         child_list = child.parent.childs.all() #go up a level and get the child list again
    # return children
#
#     def get_all_parents(self):
#         parents = [self]
#         if self.parent is not None:
#             parent = self.parent
#             parents.extend(parent.get_all_parents())
#         return parents
#
#     def clean(self):
#         if self.parent in self.get_all_children():
#             raise ValidationError("A user cannot have itself \
#                     or one of its' children as parent.")
@register.inclusion_tag('children.html')

def custom_function(independent_claim):
    # childs = independent_claim.childs.all()
    childs = get_all_children(independent_claim)
    # print(childs)

    return {'childs': childs}
