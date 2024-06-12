female(sophia).
female(sandra).
female(mia).
female(lisa).
male(peter).
male(alex).
male(dick).
male(bob).
male(andrew).
parent(bob, lisa).
parent(bob, alex).
parent(bob, sophia).
parent(mia, lisa).
parent(mia, alex).
parent(mia, sophia).
parent(peter, andrew).
parent(lisa, andrew).
parent(sophia, dick).
parent(sophia, sandra).

father(X, Y) :- X \== Y,  male(X), parent(X, Y).

sister(X, Y) :- X \== Y, female(X), parent(Z, X), parent(Z, Y).

grandmother(X, Y) :- X \== Y, female(X), parent(X, Z), parent(Z, Y).

wife_husband(X, Y) :- X \== Y, female(X), male(Y), parent(X, Z), parent(Y, Z). 

cousin(X, Y) :- X \== Y, parent(P1, X), parent(P2, Y), P1 \== P2, parent(P3, P1), parent(P3, P2).