import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_system.settings')
django.setup()

from django.contrib.auth.models import User

# Reset admin password
admin = User.objects.get(username='admin')
admin.set_password('admin123')
admin.save()
print("✓ Admin password reset to: admin123")

# Reset member password
member = User.objects.get(username='member')
member.set_password('member123')
member.save()
print("✓ Member password reset to: member123")

print("\n📝 New Login Credentials:")
print("   Admin:  admin / admin123")
print("   Member: member / member123")
