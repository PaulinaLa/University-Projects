var Node = function(n, left, right){
    this.n = n;
    this.left = left;
    this.right = right;
}

Node.prototype[Symbol.iterator] = function*(){
    yield this.n;
    if(this.left){
        yield* this.left;
    }
    if(this.right){
        yield* this.right;
    }
}

var tree = new Node(10, new Node(6, new Node(5, null, null), new Node(5, null, null)),
                        new Node(20, new Node(10, null, null), new Node(24, null, null)));
                    
for(var node of tree){
    console.log(node);
}