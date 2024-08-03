from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import UserInfo
from .validation import registervalidation
def index(request):
    return JsonResponse({'message': 'Hello world'})
@api_view(['POST'])
def upload_image(request):
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        title = request.POST.get('title', 'Untitled')
        print(photo)
        # Save the file
        # image_upload = ImageUpload.objects.create(title=title, image=photo)

        # Prepare a JSON-serializable response
        response_data = {
            'message': 'Image uploaded successfully',
            'image_url': 'testing'  # Optionally include the URL of the uploaded image
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'No file uploaded'}, status=400)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':

        if len(registervalidation(request.POST)) != 0:
            return JsonResponse({'message': registervalidation(request.POST), 'status': 0})
        else:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            address = request.POST['address']
            phone = request.POST['phone']
            birthday = request.POST['birthday']
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
            else:
                photo = 'logo.png'
            if User.objects.filter(username=username).exists():
                return JsonResponse({'message': 'Username already exists!', 'status': 0})

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Email already exists!', 'status': 0})

            if UserInfo.objects.filter(phone=phone).exists():
                return JsonResponse({'message': 'Phone already exists!', 'status': 0})

            user = User.objects.create_user(username=username, email=email, password=password1, is_staff=True, first_name=firstname, last_name=lastname)
            user.save()
            UserInfo.objects.create(user=user, address=address, phone=phone, birthday=birthday, photo=photo, role_id=1)
            return JsonResponse({'message': 'Your account has been created!', 'status': 1})

    return JsonResponse({'message': 'Cannot Accept GET Method'})

