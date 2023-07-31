print('''
LET´S PLAY CROCKET !''')

# Schleife, solange am Ende nochmal gespielt werden will
again = 'j'
while again == 'j':

    # Spielmodus wählen
    mode = input('''
Spielmodi

A   GROWING POINTS
        Rundennummer = Rundentorezahl = Rundenpunkte für Rundensieger.
        Aufsummierung der Rundenpunkte.
        (Höchste Punktzahl gewinnt.)

B   SUM UP
        Aufsummierung aller im Spiel benötigten Schläge.
        (Niedrigste Punktzahl gewinnt.)

a/b?   ''')
    if mode == 'a':
        gamename = 'GROWING POINTS'
    if mode == 'b':
        gamename = 'SUM UP'
    print()

    # Spielereingabe und Anfangswerte (für alle Spielmodi).
    name_1 = input('Spieler 1:   ')
    number_1 = 1
    score_1 = 0
    strokes_1 = 0
    player_1 = [score_1, strokes_1, number_1, name_1]

    name_2 = input('Spieler 2:   ')
    number_2 = 2
    score_2 = 0
    strokes_2 = 0
    player_2 = [score_2, strokes_2, number_2, name_2]

    player = [player_1, player_2]
    score = [score_1, score_2]

    # Weitere Anfangswerte für Modus A
    score_assigned = 0
    # falls nur 2 Spieler trotzdem nötig:
    score_3 = 0
    score_4 = 0

    more = input('Mehr Spieler? j/n   ')
    if more == 'j':
        name_3 = input('Spieler 3:   ')
        number_3 = 3
        score_3 = 0
        strokes_3 = 0
        player_3 = [score_3, strokes_3, number_3, name_3]

        score.append(score_3)
        player.append(player_3)

        more = input('Mehr Spieler? j/n   ')
        if more == 'j':
            name_4 = input('Spieler 4:   ')
            number_4 = 3
            score_4 = 0
            strokes_4 = 0
            player_4 = [score_4, strokes_4, number_4, name_4]

            score.append(score_4)
            player.append(player_4)
    print()

    # Rundenzahl
    rounds = int(input('Rundezahl: '))
    # für Modus A folgt aus Rundenzahl:
    score_total = int(0.5 * rounds * (rounds + 1))

    # Begrüßung zum Spiel
    print(f'''
::: Willkommen zu {str(rounds)} Runden {gamename}! :::

Es spielen:''')
    for x in player:
        print(f'Spieler {x[2]}: {x[3]}')
    if mode == 'a':
        print(f'''Merkt euch eure Spielernummern.
(Sie müssen für die Rundensieger eingegeben werden.)

In diesem Spiel werden bis zu {score_total} Punkte vergeben.''')
    input('>>>')

    # Spielverlauf
    # Schleife gemäß Rundennummer und (in Modus A) nur, wenn noch nicht nach Matchball beendet
    round_rec = 1
    mb_end = 0
    while round_rec <= rounds and mb_end == 0:
        if round_rec < rounds:
            print(f'\nR U N D E {str(round_rec)}')
        if round_rec == rounds:
            print(f'\nR U N D E {str(round_rec)} /// LETZTE RUNDE!')

        # MODUS A
        if mode == 'a':
            if round_rec == 1:
                print('In dieser Runde wird 1 Punkt vergeben.')
            else:
                print(f'In dieser Runde werden {str(round_rec)} Punkte vergeben.')

            # Punkte vergeben, Punktevariablen neu berechnen
            winner = int(input('Wer hat gewonnen? (1/2/3/4)  ')) - 1
            print()
            player[winner][0] += round_rec
            score_assigned += round_rec
            score_left = score_total - score_assigned

            # Punkteliste und Werte Für Berechnung von Ende nach Matchball:
            score_assigned_list = []
            for x in player:
                score_assigned_list.append(x[0])
            score_assigned_list.sort()
            score_gap = score_assigned_list[-1] - score_assigned_list[-2]

            # Ende, falls nach Matchball gewonnen
            if round_rec < rounds:
                if score_gap > score_left:
                    player.sort()
                    player.reverse()
                    print(f'''Das Spiel ist vorzeitig beendet.
Niemand kann {player[0][-1]} noch einholen.

E N D S T A N D:''')
                    for x in player:
                        print(f'{(x[-1])}: {(x[0])}')
                    print(f'{player[0][-1]} hat gewonnen!')
                    mb_end = 1
                    input('>>>')

                # ...sonst Punkte und nächsten Beginner anzeigen. Matchball?
                else:
                    print('P u n k t e s t a n d:')
                    for x in player:
                        print(f'{x[-1]}:   {x[0]}')

                    if round_rec == rounds - 1:
                        print(f'Es werden noch {str(score_left)} Punkte vergeben.\n')
                    else:
                        print(f'Es werden noch bis zu {str(score_left)} Punkte vergeben.\n')

                    print(f'{player[winner][-1]} darf das nächste Tor platzieren\nund die nächste Runde beginnen.')

                    # Hat jemand Matchball?
                    if (score_assigned_list[-1] + round_rec + 1) > (
                            score_assigned_list[-2] + score_left - round_rec + 1) \
                            and score_assigned_list[-1] != score_assigned_list[-2] \
                            and round_rec < rounds - 1:
                        player_mb = player.copy()
                        player_mb.sort()
                        print(f'+++ {player_mb[-1][-1]} hat in nächster Runde Matchball! +++')
                    input('>>>')

            # Schlussanzeige
            if round_rec == rounds:
                print('E n d s t a n d:')
                player.sort()
                player.reverse()
                for x in player:
                    print(f'{x[-1]}:   {x[0]}')
                print()
                if player[0][0] > player[1][0]:
                    print(player[0][3] + ' hat gewonnen!')
                if player[0][0] == player[1][0]:
                    print('Unentschieden!')

        # MODUS B
        if mode == 'b':

            # Punkte vergeben
            for x in player:
                x[1] = int(input(f'Wieviele Schläge brauchte {x[-1]}?   '))
                x[0] += x[1]
            print()

            # Punkte (und weiteres) anzeigen
            if round_rec < rounds:
                print('P u n k t e s t a n d:')
            if round_rec == rounds:
                print('E N D S T A N D:')
            player.sort()
            for x in player:
                print(f'{x[-1]}:   {x[0]}')
            if round_rec < rounds:
                input('>>>')
            if round_rec == rounds:
                if player[0][0] < player[1][0]:
                    print(f'{player[0][-1]} hat gewonnen!')
                if player[0][0] == player[1][0]:
                    print('Unentschieden!')
                input('>>>')

        round_rec += 1

    again = input('Noch ein Spiel? j/n   ')
print('Tschüss!')
input('>>>')
