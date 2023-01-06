:- dynamic horror/1.
:- dynamic action/1.
:- dynamic romantic/1.
:- dynamic patriotic/1.
:- dynamic murderMystery/1.

% Facts
horror(no_one_gets_out_Alive).
horror(the_conjuring).
horror(insideious).
horror(the_Ring).
horror(resident_Evil).
horror(day_of_the_dead).
horror(zombieland).

adventure(fast_and_Furious).
adventure(doom).
adventure(don).
adventure(in_the_heart_of_the_sea).
adventure(super_man).
adventure(the_adam_project).
adventure(robin_hood).

action(mad_max).
action(the_dark_night).
action(no_time_to_Die).
action(casino_Royal).
action(terminator).

romantic(the_notebook).
romantic(titanic).
romantic(nothing_hill).
romantic(jab_we_met).

patriotic(war).
patriotic(khuda_K_liyay).
patriotic(parwaz_ha_junoon).
patriotic(azaadi).
patriotic(maryam_mukhtiar).


murderMystery(sherlock_Holmes).
murderMystery(fletch).
murderMystery(you).
murderMystery(i_know_what_you_did_Last_Summer).
murderMystery(the_pink_panther).



% Rules
interest(h) :-
    findall(H, horror(H), HorrorList),
    random_member(H, HorrorList),
    write('You should watch      :: '),
    write(H),
    write('.').
interest(a) :-
    findall(A, adventure(A), AdventureList),
    random_member(A, AdventureList),
    write('You should watch    :: '),
    write(A),
    write('.').
interest(ac) :-
    findall(AC, action(AC), ActionList),
    random_member(AC, ActionList),
    write('You should watch   :: '),
    write(AC),
    write('.').
interest(r) :-
    findall(R, romantic(R), RomanticList),
    random_member(R, RomanticList),
    write('You should go watch  :: '),
    write(R),
    write('.').
interest(mm) :-
    findall(MM, murderMystery(MM), MurderMysteryList),
    random_member(MM, MurderMysteryList),
    write('You should go watch   :: '),
    write(MM),
    write('.').
interest(p) :-
    findall(P, patriotic(P), PList),
    random_member(P, PList),
    write('You should go watch   :: '),
    write(P),
    write('.').


% main fumction to run the program.
movies :-
    write('What would you like to watch'),
    nl,
    write('We have a collection of :  '),
    nl,
    write('horror'),
    nl,
    write('adventure'),
    nl,
    write('action'),
    nl,
    write('romantic'),
    nl,
    write('patriotic'),
    nl,
    write('murderMystery'),
    nl,
    write(' Select Catogery from above:: '),
    read(Response),
    ( (Response == horror)
      -> interest(h)
       ;
    (Response == adventure)
        -> interest(a)
        ;
    (Response == action)
          -> interest(ac)
         ;
    (Response == romantic)
           ->  interest(r)
           ;
    (Response == murderMystery)
           -> interest(mm)
            ;
    (Response == patriotic)
           -> interest(p)

          ;
    write('Currently unavailible!!.')).


