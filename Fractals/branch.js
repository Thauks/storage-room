function Branch(start, end) {
  this.start = start;
  this.end = end;
  this.finished = false;
  this.show = function () {
    stroke(255);
    line(this.start.x, this.start.y, this.end.x, this.end.y);
  }

  this.branchR = function () {
    var dir = p5.Vector.sub(this.end, this.start);
    dir.rotate(PI / 4);
    dir.mult(0.67);
    var newEnd = p5.Vector.add(this.end, dir);

    var right = new Branch(this.end, newEnd)
    return right;
  }

  this.branchL = function () {
    var dir = p5.Vector.sub(this.end, this.start);
    dir.rotate(-PI / 4);
    dir.mult(0.67);
    var newEnd = p5.Vector.add(this.end, dir);

    var left = new Branch(this.end, newEnd)
    return left;
  }


}
