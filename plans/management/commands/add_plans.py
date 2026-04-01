from django.core.management.base import BaseCommand
from plans.models import MembershipPlan


class Command(BaseCommand):
    help = 'Add sample membership plans'

    def handle(self, *args, **options):
        # Clear existing plans
        MembershipPlan.objects.all().delete()

        plans_data = [
            {
                'name': 'Starter',
                'slug': 'starter',
                'price': '2999',
                'duration_months': 1,
                'description': 'Perfect for beginners looking to start their fitness journey',
                'features': 'Unlimited facility access\nAll equipment available\nBasic member app',
                'is_featured': False,
                'color_label': 'primary',
            },
            {
                'name': 'Premium',
                'slug': 'premium',
                'price': '4999',
                'duration_months': 3,
                'description': 'Our most popular plan with group classes and training',
                'features': 'Unlimited facility access\nAll equipment available\nGroup classes included\nMember app access\n4 personal training sessions/month\nNutrition guidance',
                'is_featured': True,
                'color_label': 'secondary',
            },
            {
                'name': 'Elite',
                'slug': 'elite',
                'price': '7999',
                'duration_months': 6,
                'description': 'Complete fitness solution with dedicated coaching',
                'features': 'Unlimited facility access\nAll equipment available\nUnlimited group classes\nFull member app\nUnlimited personal training\nNutrition & meal planning\nPerformance tracking\nPriority support',
                'is_featured': False,
                'color_label': 'secondary',
            },
            {
                'name': 'Annual Pass',
                'slug': 'annual',
                'price': '49999',
                'duration_months': 12,
                'description': 'Best value - save 30% with annual commitment',
                'features': 'Everything in Elite plan\nUnlimited facility access\nUnlimited group classes\nFull member app\nUnlimited personal training\nNutrition & meal planning\nPerformance tracking\nPriority 24/7 support\nFree merchandise\nVIP lounge access',
                'is_featured': False,
                'color_label': 'primary',
            },
        ]

        for plan_data in plans_data:
            plan_data['is_active'] = True
            MembershipPlan.objects.create(**plan_data)
            self.stdout.write(self.style.SUCCESS(f'Created plan: {plan_data["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully added membership plans!'))
