from django.core.management.base import BaseCommand
from core.models import Equipment, Facility


class Command(BaseCommand):
    help = 'Add sample facilities and equipment'

    def handle(self, *args, **options):
        # Clear existing data
        Facility.objects.all().delete()
        Equipment.objects.all().delete()

        # Create Facilities
        facilities_data = [
            {
                'name': 'Cardio Zone',
                'zone_type': 'cardio',
                'description': 'High-tech cardio machines with integrated performance tracking and climate control.',
                'capacity': 30,
                'features': 'Treadmills, Ellipticals, Stationary Bikes, Rowing Machines, Heart Rate Monitoring',
                'operating_hours': '6:00 AM - 11:00 PM',
                'photo': None
            },
            {
                'name': 'Weight Training Area',
                'zone_type': 'weights',
                'description': 'Comprehensive free weight and machine training area for strength development.',
                'capacity': 40,
                'features': 'Dumbbells, Barbells, Weight Racks, Benches, Olympic Platforms',
                'operating_hours': '6:00 AM - 11:00 PM',
                'photo': None
            },
            {
                'name': 'Functional Training',
                'zone_type': 'functional',
                'description': 'Dynamic functional training space for compound movements and athletic training.',
                'capacity': 25,
                'features': 'TRX Suspension, Medicine Balls, Kettlebells, Battle Ropes, Agility Cones',
                'operating_hours': '6:00 AM - 10:30 PM',
                'photo': None
            },
            {
                'name': 'Yoga & Stretching Studio',
                'zone_type': 'yoga',
                'description': 'Serene studio designed for flexibility, mindfulness, and recovery training.',
                'capacity': 20,
                'features': 'Yoga Mats, Blocks, Straps, Bolsters, Mirrors, Climate Controlled',
                'operating_hours': '7:00 AM - 9:00 PM',
                'photo': None
            },
        ]

        for facility_data in facilities_data:
            Facility.objects.create(**facility_data)
            self.stdout.write(self.style.SUCCESS(f'Created facility: {facility_data["name"]}'))

        # Create Equipment
        equipment_data = [
            # Cardio
            {'name': 'Treadmill Pro X', 'category': 'cardio', 'description': 'Advanced treadmill with AI-powered coaching and personalized training programs.', 'specifications': 'Speed: 0-20 mph, Incline: 0-15%', 'quantity': 5, 'status': 'active'},
            {'name': 'Elliptical Machine', 'category': 'cardio', 'description': 'Low-impact full-body cardio machine with adjustable resistance.', 'specifications': '20 Resistance Levels', 'quantity': 4, 'status': 'active'},
            {'name': 'Stationary Bike Elite', 'category': 'cardio', 'description': 'Premium stationary bike with immersive training apps and performance metrics.', 'specifications': 'Magnetic Resistance, Bluetooth Enabled', 'quantity': 6, 'status': 'active'},
            {'name': 'Rowing Machine', 'category': 'cardio', 'description': 'Full-body cardio and strength machine with realistic rowing mechanics.', 'specifications': '300 lb Max Weight', 'quantity': 3, 'status': 'active'},

            # Strength
            {'name': 'Adjustable Dumbbells', 'category': 'strength', 'description': 'Space-saving adjustable dumbbells ranging from light to heavy weights.', 'specifications': '5 lbs - 100 lbs', 'quantity': 1, 'status': 'active'},
            {'name': 'Olympic Barbell', 'category': 'strength', 'description': 'Professional-grade barbells for heavy compound lifts.', 'specifications': '45 lbs, 7 ft', 'quantity': 8, 'status': 'active'},
            {'name': 'Squat Rack', 'category': 'strength', 'description': 'Heavy-duty squat rack with adjustable safety bars and pin heights.', 'specifications': '1000 lbs Capacity', 'quantity': 3, 'status': 'active'},
            {'name': 'Bench Press', 'category': 'strength', 'description': 'Adjustable weight bench for flat, incline, and decline exercises.', 'specifications': 'Multi-Position', 'quantity': 4, 'status': 'active'},

            # Functional
            {'name': 'Kettlebell Set', 'category': 'functional', 'description': 'Complete kettlebell set for cardio and strength training.', 'specifications': '10 lbs - 80 lbs', 'quantity': 1, 'status': 'active'},
            {'name': 'TRX Suspension System', 'category': 'functional', 'description': 'Suspension training system for bodyweight resistance exercises.', 'specifications': 'Adjustable Straps', 'quantity': 5, 'status': 'active'},
            {'name': 'Medicine Ball', 'category': 'functional', 'description': 'Weighted medicine balls for core and explosive power training.', 'specifications': '4 lbs - 25 lbs', 'quantity': 2, 'status': 'active'},
            {'name': 'Battle Ropes', 'category': 'functional', 'description': 'Heavy-duty battle ropes for intense cardio and conditioning.', 'specifications': '50 ft Length, 2 inch Diameter', 'quantity': 2, 'status': 'active'},

            # Flexibility
            {'name': 'Yoga Mat Premium', 'category': 'flexibility', 'description': 'Eco-friendly yoga mat with superior grip and cushioning.', 'specifications': '8mm Thickness, Non-Slip', 'quantity': 20, 'status': 'active'},
            {'name': 'Foam Roller', 'category': 'flexibility', 'description': 'High-density foam roller for muscle recovery and myofascial release.', 'specifications': '12 inch x 36 inch', 'quantity': 10, 'status': 'active'},
            {'name': 'Resistance Bands Set', 'category': 'flexibility', 'description': 'Color-coded resistance bands for flexibility and strength training.', 'specifications': 'Light, Medium, Heavy, Extra Heavy', 'quantity': 15, 'status': 'active'},

            # Recovery
            {'name': 'Massage Gun', 'category': 'recovery', 'description': 'Percussive massage therapy device for muscle recovery.', 'specifications': '4000 RPM, 5 Attachments', 'quantity': 4, 'status': 'active'},
            {'name': 'Ice Bath Tub', 'category': 'recovery', 'description': 'Cold water immersion therapy for athletic recovery.', 'specifications': 'Chiller System Included', 'quantity': 1, 'status': 'active'},
            {'name': 'Stretching Station', 'category': 'recovery', 'description': 'Dedicated stretching equipment for post-workout recovery.', 'specifications': 'Multiple Positions', 'quantity': 2, 'status': 'active'},
        ]

        for equipment in equipment_data:
            Equipment.objects.create(**equipment)
            self.stdout.write(self.style.SUCCESS(f'Created equipment: {equipment["name"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully added facilities and equipment!'))
