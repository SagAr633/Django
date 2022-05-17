from django.shortcuts import redirect

def sigin_required(fn):
    def wrapper(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
        return wrapper
