from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Test admin login
admin_user = authenticate(username='admin', password='admin@123')
if admin_user:
    print("✓ Admin login works!")
else:
    print("✗ Admin login failed!")
    try:
        user = User.objects.get(username='admin')
        print(f"  User exists: {user.username}")
    except User.DoesNotExist:
        print("  User doesn't exist")

# Test member login
member_user = authenticate(username='member', password='member@123')
if member_user:
    print("✓ Member login works!")
else:
    print("✗ Member login failed!")
    try:
        user = User.objects.get(username='member')
        print(f"  User exists: {user.username}")
    except User.DoesNotExist:
        print("  User doesn't exist")
