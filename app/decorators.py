from django.http import HttpResponseNotFound

def requires_role(roles):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs) :
            if not request.user.role in roles:
                return HttpResponseNotFound()
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper