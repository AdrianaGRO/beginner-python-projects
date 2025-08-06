## Start
=> ASK: Would you like to play BT? > user_wants_to_play

=> if user_wants_to_play then:
        => print logo
        => computer random choice (2 cards)
        => calculate computer score
        => player random choice (1 card)
        => declare user_wants_another_card = True
        => calculate player's score user_exceeds_21
                    => if user_exceeds_21 then:
                    => display busted
                    => if not user_exceed_21 then:
                    => ASK: Would you like to get another card? > user_wants_another_card
        => display result
        ASK: Would you like to play BT?

=> exit



