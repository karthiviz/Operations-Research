var 0..10: x;

constraint x mod 4 = 0;

solve minimize (x-7)^2;

output ["x: \(x)\nObj: \((x-7)^2)"]