var fws = [];
var gravity;

function setup() {
  createCanvas(1910, 952);
  colorMode(HSB);
  gravity = createVector(0, 0.2);
  fws.push(new Firework());
  stroke(255);
  strokeWeight(4);
  background(0);
}

function draw() {
  colorMode(RGB);
  background(3,3,3,18);
  if (random(1) < 0.02) {
    fws.push(new Firework());
  }
  for (var i = fws.length - 1; i >= 0; i--) {
    fws[i].update();
    fws[i].show();
    if (fws[i].done()) {
      fws.splice(i, 1);
    }
  }


}
