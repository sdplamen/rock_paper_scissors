from django import forms

class PlayerChoiceForm(forms.Form):
    MOVE_CHOICES = [
        ('rock', 'Rock'),
        ('paper', 'Paper'),
        ('scissors', 'Scissors'),
    ]
    player_move = forms.ChoiceField(
        choices=MOVE_CHOICES,
        widget=forms.RadioSelect,
        label="Choose your move"
    )