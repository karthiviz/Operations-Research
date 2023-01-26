array[int] of int: readings;
int: start;
int: n = length(readings);
set of int: HOUR = 1..n;
set of int: HOUR0 = 0..n;
enum ACTION = {heat, strongly_heat, cool, strongly_cool, do_nothing};
array[ACTION] of int: adjust = [1, 4, -2, -5, 0];
array[ACTION] of int: cost = [1, 5, 3, 9, 0];

array[HOUR] of var ACTION: choice;
array[HOUR0] of var 25..30: temp;

constraint temp[0] = start;

constraint forall(h in HOUR)
                 (temp[h] = (temp[h-1] + readings[h]) div 2 + adjust[choice[h]]);

var int: c = sum(h in HOUR)
                     (cost[choice[h]]);
                                
solve minimize c;

output ["temp = \(temp);\nCost = \(c)\n"];
