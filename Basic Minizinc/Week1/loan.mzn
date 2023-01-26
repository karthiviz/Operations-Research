var float: P;  % Principal amount of the loan
var float: R;  % Quarterly repayment amount
var 0.0 .. 2.0: I;   % Interest rate on the loan

var float: B1;
var float: B2;
var float: B3;
var float: B4;

constraint B1 = P * (1.0 + I) - R;
constraint B2 = B1 * (1.0 + I) - R;
constraint B3 = B2 * (1.0 + I) - R;
constraint B4 = B3 * (1.0 + I) - R;

solve satisfy;

output ["R: \(R)"]