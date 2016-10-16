from django import forms


from models import Workout_Event


class CreateForm(forms.ModelForm):

    class Meta:
        model = Workout_Event
        fields = ('event_name', 'event_type', 'location', 'date',
                  'time_start', 'time_end', 'workout_description',
                  'experience_level', 'number_of_spots',)
