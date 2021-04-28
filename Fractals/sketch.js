var tree = [];

function setup() {
  createCanvas(800, 800);
  var a = createVector(width / 2, height);
  var b = createVector(width / 2, height - 200);
  var root = new Branch(a, b);

  tree[0] = root;
}

function mousePressed() {
  for (var i = tree.length - 1; i >= 0; i--) {
    if(!tree[i].finished){
    tree.push(tree[i].branchL());
    tree.push(tree[i].branchR());
    }
    tree[i].finished = true;
  }

  tree[1] = tree[0].branchL();
  tree[2] = tree[0].branchR();
}

function draw() {
  background(51);
  for (var i = 0; i < tree.length; i++) {
    tree[i].show();
  }
}
