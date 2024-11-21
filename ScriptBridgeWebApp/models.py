from django.db import models


from django.db import models

class ProgrammingQuestion(models.Model):
    # Define language choices as a tuple of tuples
    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('C', 'C'),
    ]

    sr_no = models.AutoField(primary_key=True)  # Auto-incrementing serial number
    question = models.TextField()  # Stores programming-related questions
    answer = models.TextField()  # Stores code/program solutions
    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,  # Dropdown options
        default='C'  # Default option
    )

    def __str__(self):
        return f"Q{self.sr_no}: {self.question[:50]}... [{self.language}]"