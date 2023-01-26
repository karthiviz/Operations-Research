enum PRODUCT;
array[PRODUCT] of float: power;

enum RESOURCE;
array[RESOURCE] of float: capacity;

array[PRODUCT,RESOURCE] of float: consumption;

array[PRODUCT] of var int: produce;

constraint forall(p in PRODUCT)(produce[p] >= 0);

constraint forall(r in RESOURCE)(
  sum(p in PRODUCT)(consumption[p,r] * produce[p]) <= capacity[r]);
  
solve maximize sum(p in PRODUCT)(power[p] * produce[p]);

output ["\(p): \(produce[p]) \n" | p in PRODUCT];
output ["Power: \(sum(p in PRODUCT)(power[p] * produce[p]))"]
