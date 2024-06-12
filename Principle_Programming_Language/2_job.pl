job(len,plastic_surgeon).
job(lance,heart_surgeon).
job(frank,brain_surgeon).
job(charlie,plastic_surgeon).
job(lisa,doctor).
address(joe,hanoi).
address(sam,hanoi).
address(bill,danang).
address(cindy,ninhbinh).
address(joan,tphcm).
address(len,hanoi).
address(lance,nhatrang).
address(frank,danang).
address(charlie,hanoi).
address(lisa,hanoi).
salary(joe,5).
salary(sam,15).
salary(bill,20).
salary(cindy,14).
salary(joan,8).
salary(len,4).
salary(lance,6.5).
salary(frank,8.5).
salary(charlie,12).
salary(lisa,19).

who(X, Add) :- address(X,Add).

find_job(X, Y) :- job(X, Z), split_string(Z, "_", "", Y).

find_surgeon(X, T) :- find_job(X, G), member(T, G).

find_surgeon_by_place(X, Job, Place) :- find_surgeon(X, Job), address(X, Place). 

find_surgeon_by_place_salary(X, Job, Place, Salary) :- find_surgeon_by_place(X, Job, Place), salary(X, S), S > Salary.