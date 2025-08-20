from rest_framework import serializers


class GamePlaySerializer(serializers.Serializer):
    player_move = serializers.ChoiceField(
        choices=['rock', 'paper', 'scissors'],
        help_text="Choose 'rock', 'paper', or 'scissors'"
    )

class GameResultSerializer(serializers.Serializer):
    player_move = serializers.CharField()
    computer_move = serializers.CharField()
    result_message = serializers.CharField()
    win = serializers.IntegerField()
    lost = serializers.IntegerField()
    draw = serializers.IntegerField()