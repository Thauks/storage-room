function Firework() {
  
  this.hu = random (3, 255);
  this.fw = new Particle(random(width), height, true, this.hu);
  this.exploded = false;
  this.particles = [];
  
  this.update = function () {
    if (!this.exploded) {
      this.fw.applyForce(gravity);
      this.fw.update();
      if (this.fw.vel.y >= 0) {
        this.exploded = true;
        this.explode();
      }
    }

    for (var i = this.particles.length - 1; i >= 0; i--) {
      this.particles[i].applyForce(gravity);
      this.particles[i].update();
      if (this.particles[i].done()) {
        this.particles.splice(i, 1);
      }
    }
  }

  this.explode = function () {
    for (var i = 0; i < 100; i++) {
      var p = new Particle(this.fw.pos.x, this.fw.pos.y, false, this.hu);
      this.particles.push(p);
    }
  }

  this.done = function () {
    if (this.exploded && this.particles.length === 0) {
      return true;
    } else {
      return false;
    }
  }

  this.show = function () {
    if (!this.exploded) {
      this.fw.show();
    }
    if (this.exploded) {
      for (var i = 0; i < this.particles.length; i++) {
        this.particles[i].show();
      }
    }
  }
}
