// push
const push = (stack, item) => [item, ...stack];

// pop
const pop = (stack) => stack.slice(1);

// peek
const peek = (stack) => stack[0];

// isEmpty
const isEmpty = (stack) => !stack.length;

// size
const size = (stack) => stack.length;

// testing
let stack = [];

console.log(isEmpty(stack));

stack = push(stack, 1);
console.log(stack);
stack = push(stack, 2);
console.log(stack);
stack = push(stack, 3);
console.log(stack);
stack = push(stack, 4);
console.log(stack);
stack = push(stack, 5);
console.log(stack);

console.log(peek(stack));
console.log(size(stack));
console.log(isEmpty(stack));

stack = pop(stack);
stack = pop(stack);
stack = pop(stack);
stack = pop(stack);

console.log(isEmpty(stack));
console.log(peek(stack));
stack = pop(stack);
console.log(isEmpty(stack));
console.log(size(stack));
