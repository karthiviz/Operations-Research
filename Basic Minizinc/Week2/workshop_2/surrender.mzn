% workshop 2
% select a set of trade negotiation party
enum NEGOTIATOR;
NEGOTIATOR: dummy; 

int: l; % minimum party size
int: u; % maximum party size
int: m; % minimum joint ability

array[NEGOTIATOR] of int: honor;
array[NEGOTIATOR,NEGOTIATOR] of int: joint;

var set of NEGOTIATOR: party;

constraint not(dummy in party);
constraint card(party) >= l;
constraint card(party) <= u;
constraint sum(i,j in party where i<j)(joint[i,j]) >= m;

var int: obj = min([honor[i] | i in party]);
solve minimize obj;

output ["party = \(party)\nobj = \(obj)"]


