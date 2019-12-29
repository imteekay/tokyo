class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items = [item, ...this.items];
  }

  pop() {
    if (this.isEmpty()) {
      return;
    }

    const poppedItem = this.items[0];
    this.items = this.items.slice(1);
    return poppedItem;
  }

  top() {
    return this.items[0];
  }

  isEmpty() {
    return this.items[0] === undefined;
  }

  size() {
    return this.items.length;
  }
}

// testing
const stack = new Stack();

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

console.log(stack.isEmpty());
console.log(stack.top());

console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());

console.log(stack.isEmpty());

console.log(stack.pop());

console.log(stack.isEmpty());
console.log(stack.top());
