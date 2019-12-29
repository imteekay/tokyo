const createStack = () => {
  const items = [];

  const push = (item) => [item, ...items];
  const pop = () => items.slice(1);
  const top = () => items[0];
  const isEmpty = () => !items.length;
  const size = () => items.length;

  return {
    push,
    pop,
    top,
    isEmpty,
    size
  };
};

// testing
const stack = createStack();

console.log(stack.isEmpty());

stack.push(1);
console.log(stack.items);
stack.push(2);
console.log(stack.items);
stack.push(3);
console.log(stack.items);
stack.push(4);
console.log(stack.items);
stack.push(5);
console.log(stack.items);

console.log(stack.top());
console.log(stack.size());
console.log(stack.isEmpty());

stack.pop();
stack.pop();
stack.pop();
stack.pop();

console.log(stack.isEmpty());
console.log(stack.top());
stack.pop();
console.log(stack.isEmpty());
console.log(stack.size());
