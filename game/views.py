from django.shortcuts import render
from random import randint
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from game.forms import PlayerChoiceForm
from game.serializers import GamePlaySerializer, GameResultSerializer


# Create your views here.
def game_view(request):
    if 'win' not in request.session:
        request.session['win'] = 0
    if 'lost' not in request.session:
        request.session['lost'] = 0
    if 'draw' not in request.session:
        request.session['draw'] = 0

    player_move_display = ""
    computer_move_display = ""
    result_message = ""

    if request.method == 'POST':
        form = PlayerChoiceForm(request.POST)
        if form.is_valid():
            player_choice = form.cleaned_data['player_move']

            if player_choice == 'rock':
                player_move_display = 'Rock'
            elif player_choice == 'paper':
                player_move_display = 'Paper'
            else:
                player_move_display = 'Scissors'

            computer_random_number = randint(1, 3)
            if computer_random_number == 1:
                computer_move = 'rock'
                computer_move_display = 'Rock'
            elif computer_random_number == 2:
                computer_move = 'paper'
                computer_move_display = 'Paper'
            else:
                computer_move = 'scissors'
                computer_move_display = 'Scissors'

            if (player_choice == 'rock' and computer_move == 'scissors') or \
               (player_choice == 'paper' and computer_move == 'rock') or \
               (player_choice == 'scissors' and computer_move == 'paper'):
                request.session['win'] += 1
                result_message = "You win!"
            elif player_choice == computer_move:
                request.session['draw'] += 1
                result_message = "It's a draw!"
            else:
                request.session['lost'] += 1
                result_message = "You lost!"
    else:
        form = PlayerChoiceForm()

    context = {
        'form': form,
        'win': request.session['win'],
        'lost': request.session['lost'],
        'draw': request.session['draw'],
        'player_move': player_move_display,
        'computer_move': computer_move_display,
        'result_message': result_message,
    }

    return render(request, 'index.html', context)

class GameAPIView(APIView):
    serializer_class = GameResultSerializer
    def post(self, request, format=None):
        serializer = GamePlaySerializer(data=request.data)
        if serializer.is_valid():
            player_choice = serializer.validated_data['player_move']

            if 'win' not in request.session:
                request.session['win'] = 0
            if 'lost' not in request.session:
                request.session['lost'] = 0
            if 'draw' not in request.session:
                request.session['draw'] = 0

            player_move_display = player_choice.capitalize()

            moves = ['rock', 'paper', 'scissors']
            computer_move = moves[randint(0, 2)]
            computer_move_display = computer_move.capitalize()

            result_message = ""
            if (player_choice == 'rock' and computer_move == 'scissors') or \
               (player_choice == 'paper' and computer_move == 'rock') or \
               (player_choice == 'scissors' and computer_move == 'paper'):
                request.session['win'] += 1
                result_message = "You win!"
            elif player_choice == computer_move:
                request.session['draw'] += 1
                result_message = "'It's a draw!'"
            else:
                request.session['lost'] += 1
                result_message = 'You lost!'

            response_data = {
                'player_move': player_move_display,
                'computer_move': computer_move_display,
                'result_message': result_message,
                'win': request.session['win'],
                'lost': request.session['lost'],
                'draw': request.session['draw'],
            }

            result_serializer = GameResultSerializer(response_data)
            return Response(result_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        response_data = {
            'player_move': '',
            'computer_move': '',
            'result_message': '',
            'win': request.session.get('win', 0),
            'lost': request.session.get('lost', 0),
            'draw': request.session.get('draw', 0),
        }
        result_serializer = GameResultSerializer(response_data)
        return Response(result_serializer.data, status=status.HTTP_200_OK)