"""
Seed command: populates the database with realistic sample data.
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seeds the database with sample gym data'

    def handle(self, *args, **options):
        from plans.models import MembershipPlan
        from members.models import Member
        from payments.models import Payment
        from attendance.models import Attendance

        self.stdout.write(self.style.MIGRATE_HEADING('🏋️  Seeding KINETIC PULSE database...'))

        # ── 1. Create Membership Plans ──────────────────────────────────────
        plans_data = [
            {
                'name': 'Standard',
                'slug': 'standard',
                'price': 999,
                'duration_months': 1,
                'description': 'Perfect for beginners',
                'features': '24/7 Access\nStandard Equipment\nLocker Room Access',
                'is_featured': False,
                'color_label': 'outline',
            },
            {
                'name': 'Premium',
                'slug': 'premium',
                'price': 2499,
                'duration_months': 1,
                'description': 'Best value for regular members',
                'features': '24/7 Access\nAll Equipment\nPersonal Training (2x/mo)\nRecovery Zone\nLocker Room',
                'is_featured': True,
                'color_label': 'primary',
            },
            {
                'name': 'Elite Performance',
                'slug': 'elite',
                'price': 4999,
                'duration_months': 1,
                'description': 'The ultimate gym experience',
                'features': '24/7 VIP Access\nUnlimited Personal Training\nSpa & Cryotherapy\nNutrition Coaching\nBiometric Tracking\nGuest Passes (2/mo)',
                'is_featured': False,
                'color_label': 'secondary',
            },
            {
                'name': 'Annual Standard',
                'slug': 'annual-standard',
                'price': 8999,
                'duration_months': 12,
                'description': 'Best price per month — commit yearly',
                'features': '24/7 Access\nStandard Equipment\nLocker Room\n2 Months Free',
                'is_featured': False,
                'color_label': 'tertiary',
            },
        ]

        plans = {}
        for pdata in plans_data:
            plan, created = MembershipPlan.objects.get_or_create(slug=pdata['slug'], defaults=pdata)
            plans[pdata['slug']] = plan
            if created:
                self.stdout.write(f'  ✓ Plan: {plan.name}')

        # ── 2. Create Members ────────────────────────────────────────────────
        members_data = [
            ('Marcus', 'Thorne', 'marcus.thorne@email.com', '+91 9876543210', 'elite', 'active', -5),
            ('Elena', 'Rodriguez', 'elena.r@email.com', '+91 9876543211', 'premium', 'active', -2),
            ('Jordan', 'Smith', 'jordan.smith@email.com', '+91 9876543212', 'standard', 'expired', -45),
            ('Sarah', 'Jenkins', 'sarah.j@email.com', '+91 9876543213', 'premium', 'pending', -1),
            ('David', 'Rossi', 'david.rossi@email.com', '+91 9876543214', 'elite', 'active', -10),
            ('Aisha', 'Patel', 'aisha.patel@email.com', '+91 9876543215', 'standard', 'active', -20),
            ('Ryan', 'Nakamura', 'ryan.n@email.com', '+91 9876543216', 'annual-standard', 'active', -90),
            ('Priya', 'Mehta', 'priya.m@email.com', '+91 9876543217', 'premium', 'active', -15),
            ('Lucas', 'Wade', 'lucas.w@email.com', '+91 9876543218', 'standard', 'expired', -60),
            ('Sofia', 'Chen', 'sofia.chen@email.com', '+91 9876543219', 'elite', 'active', -3),
        ]

        created_members = []
        today = date.today()
        for fname, lname, email, phone, plan_slug, status, days_ago in members_data:
            join = today + timedelta(days=days_ago)
            plan = plans.get(plan_slug)
            expiry = join + timedelta(days=plan.duration_months * 30) if plan else None
            member, created = Member.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': fname,
                    'last_name': lname,
                    'phone': phone,
                    'plan': plan,
                    'status': status,
                    'join_date': join,
                    'membership_expiry': expiry,
                }
            )
            created_members.append(member)
            if created:
                self.stdout.write(f'  ✓ Member: {member.get_full_name()} [{member.member_id}]')

        # ── 3. Create Payments ───────────────────────────────────────────────
        active_members = [m for m in created_members if m.status == 'active']
        methods = ['cash', 'upi', 'card', 'online']
        for member in active_members:
            if member.plan:
                # 1-3 payments per active member
                for i in range(random.randint(1, 3)):
                    pay_date = today - timedelta(days=i * 30 + random.randint(0, 5))
                    Payment.objects.get_or_create(
                        member=member,
                        payment_date=pay_date,
                        defaults={
                            'plan': member.plan,
                            'amount': member.plan.price,
                            'payment_method': random.choice(methods),
                            'status': 'paid',
                            'transaction_id': f'TXN{random.randint(100000, 999999)}',
                        }
                    )
        self.stdout.write(f'  ✓ Payments created for {len(active_members)} members')

        # ── 4. Create Attendance ─────────────────────────────────────────────
        zones = ['main_hall', 'zone_b', 'cardio_zone', 'weight_room', 'yoga_room']
        activities = ['general', 'hiit', 'cardio', 'powerlifting', 'yoga', 'leg_day', 'upper_body']
        now = timezone.now()

        for member in active_members:
            # Past week attendance (1-5 sessions)
            for day_offset in range(random.randint(1, 7)):
                checkin_dt = now - timedelta(days=day_offset, hours=random.randint(6, 20), minutes=random.randint(0, 59))
                checkout_dt = checkin_dt + timedelta(hours=random.randint(1, 2), minutes=random.randint(0, 45))
                Attendance.objects.create(
                    member=member,
                    check_in=checkin_dt,
                    check_out=checkout_dt,
                    zone=random.choice(zones),
                    activity=random.choice(activities),
                )

            # Today's active check-in (no checkout) for ~half of active members
            if random.random() > 0.5:
                Attendance.objects.create(
                    member=member,
                    check_in=now - timedelta(minutes=random.randint(10, 90)),
                    check_out=None,
                    zone=random.choice(zones),
                    activity=random.choice(activities),
                )

        self.stdout.write(f'  ✓ Attendance records seeded')

        self.stdout.write(self.style.SUCCESS('\n✅ Database seeded successfully!'))
        self.stdout.write(self.style.SUCCESS(f'   Plans: {MembershipPlan.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   Members: {Member.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   Payments: {Payment.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'   Attendance: {Attendance.objects.count()}'))
        self.stdout.write('')
        self.stdout.write('👤 Create a superuser to log in:')
        self.stdout.write('   python manage.py createsuperuser')
