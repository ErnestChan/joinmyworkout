from django import forms


from models import Workout_Event


class CreateForm(forms.ModelForm):

    class Meta:
        model = Workout_Event
        fields =('name', 'type', 'location', 'date', 'start', 'end',
            'description', 'experience level', 'spots')