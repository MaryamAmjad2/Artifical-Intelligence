canCook(maryam).
canCook(misbah).
canCook(sofia).
girl(maryam).

sing_a_song(maryam).
listen_music(maryam).
happy(maryam):-sing_a_song(maryam).


likes(cooking,sofia):-canCook(sofia).


female(sarah).
female(rose).
female(milly).

male(jhon).
male(jhosh).

playsGuitar(misbah).
happy(misbah):-playsGuitar(misbah).
