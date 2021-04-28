function Particle(x, y, f, hu) {
  this.f = f;
  this.hu = hu;
  this.pos = createVector(x, y);
  this.lifespan = 255;

  if (this.f) {
    this.vel = createVector(0, random(-20, -12));
  } else {
    this.vel = p5.Vector.random2D();
    this.vel.mult(random(5, 30));
  }

  this.acc = createVector(0, 0);

  this.applyForce = function (force) {
    this.acc.add(force);
  }

  this.update = function () {
    if (!this.f) {
      this.vel.mult(0.9);
      this.lifespan -= 3;
    }

    this.vel.add(this.acc);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }
  
  this.done = function(){
    if (this.lifespan < 0){
      return true;
    }else{
      return false;
    }
  }

  this.show = function () {
    colorMode(HSB);
    if (!this.f){
      strokeWeight(2);
      stroke(this.hu,255,255, this.lifespan);
    }else{
      strokeWeight(4);
      stroke(255,0,255);
    }
    point(this.pos.x, this.pos.y);
  }
}
