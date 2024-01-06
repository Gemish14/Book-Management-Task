from home.models import Student
def get_logged_in_user(request):
    student = None
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        try:
            student = Student.objects.get(stud_id=user_id)
        except Student.DoesNotExist:
            pass

    return {'student': student}