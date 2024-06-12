gcd(0, X, X) :-!.
gcd(X, 0, X) :-!.
gcd(X, X, X) :-!.
gcd(A, B, X) :- A > B, gcd(B, A, X).
gcd(A, B, X) :- A < B, Y is B mod A, gcd(Y, A, X).

