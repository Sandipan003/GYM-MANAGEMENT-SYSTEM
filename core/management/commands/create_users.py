"""
Management command to create test users for admin and member login.
Usage: python manage.py create_users
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from members.models import Member


class Command(BaseCommand):
    help = 'Creates test users for admin and member login'

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('👤 Creating test users...'))

        # Create Admin User
        admin_username = 'admin'
        admin_password = 'admin@123'
        
        if not User.objects.filter(username=admin_username).exists():
            admin_user = User.objects.create_superuser(
                username=admin_username,
                email='admin@kineticpulse.com',
                password=admin_password,
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(
                self.style.SUCCESS(f'✓ Admin created: username={admin_username}, password={admin_password}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'✓ Admin already exists: username={admin_username}')
            )

        # Create Member User
        member_username = 'member'
        member_password = 'member@123'
        member_email = 'member@kineticpulse.com'
        
        if not User.objects.filter(username=member_username).exists():
            member_user = User.objects.create_user(
                username=member_username,
                email=member_email,
                password=member_password,
                first_name='Test',
                last_name='Member'
            )
            
            # Create associated Member profile
            from plans.models import MembershipPlan
            from datetime import date, timedelta
            
            default_plan = MembershipPlan.objects.filter(is_active=True).first()
            if default_plan:
                Member.objects.get_or_create(
                    email=member_email,
                    defaults={
                        'first_name': 'Test',
                        'last_name': 'Member',
                        'phone': '+91 1234567890',
                        'user': member_user,
                        'plan': default_plan,
                        'status': 'active',
                        'join_date': date.today(),
                        'membership_expiry': date.today() + timedelta(days=30)
                    }
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Member created: username={member_username}, password={member_password}')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'✓ Member already exists: username={member_username}')
            )

        self.stdout.write(self.style.SUCCESS('\n✅ All users created successfully!\n'))
        self.stdout.write(self.style.WARNING('📝 Login Credentials:'))
        self.stdout.write(f'   Admin:  username={admin_username}, password={admin_password}')
        self.stdout.write(f'   Member: username={member_username}, password={member_password}')
