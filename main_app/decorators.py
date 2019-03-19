from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

<<<<<<< HEAD
def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login')
# Decorator for views that checks that the loggin in user is a student,
# redirects to the log-in page if necessary
actual_decorator = user_passes_test(
    lambda u: u.is_active and u.is_student,
    login_url = login_url,
    redirect_field_name=redirect_field_name
)
if function:
    return actual_decorator(function)
return actual_decorator

def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    #decorator for views that checks that the logged in user is a teacher,
    # redirects to the log-in page if necessary.

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_teacher,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
=======
# def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login')
# # Decorator for views that checks that the loggin in user is a student,
# # redirects to the log-in page if necessary
# actual_decorator = user_passes_test(
#     lambda u: u.is_active and u.is_student,
#     login_url = login_url,
#     redirect_field_name=redirect_field_name
# )
# if function:
#     return actual_decorator(function)
# return actual_decorator

# def teacher_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
#     #decorator for views that checks that the logged in user is a teacher,
#     # redirects to the log-in page if necessary.

#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_teacher,
#         login_url=login_url,
#         redirect_field_name=redirect_field_name
#     )
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
>>>>>>> 63973a88048828ad4a0b8b416d31834e1eecb55c


