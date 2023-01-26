enum MOVES;
int: time;
array[MOVES] of int: power;
array[MOVES] of int: duration;
var set of MOVES: occur;

constraint (sum(i in occur)(duration[i])) <= time;

solve maximize sum(i in occur)(power[i]); 