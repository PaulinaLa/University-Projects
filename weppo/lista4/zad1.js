var Node = function(n, left, right){
    this.n = n;
    this.left = left;
    this.right = right;
}

var tree = new Node(6, new Node(4, new Node(2, null, null), new Node(5, null, null)),
                        new Node(10, new Node(8, null, null), new Node(15, null, null)));

console.log(tree);