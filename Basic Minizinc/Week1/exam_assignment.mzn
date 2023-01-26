enum day = {Monday, Tuesday, Wednesday};

var day: A;
var day: B;
var day: C;
var day: D;
var day: E;
var day: F;
var day: G;

constraint A != B;
constraint A != C;
constraint B != C;
constraint B != D;
constraint B != E;
constraint C != E;
constraint C != F;
constraint D != E;
constraint E != F;
constraint E != G;
constraint F != G;

solve satisfy;
