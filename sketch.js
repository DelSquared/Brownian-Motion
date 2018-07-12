var x = 0; //position along x axis
var w=700; //canvas width
var h=300; //canvas height
var n = 1000; //number of particles per lap
var sigma = 1; //"variance" of random walk
var xo=new Array(n); //particle positions
var bars=60; //no. of bars in histogram
var amp=250; //histogram amplitude
var histogram=new Array(bars) //histogram
for (i = 0; i < bars; i++) {
    histogram[i]=0; //setting histo to 0
}
for (i = 0; i < n; i++) {
    xo[i]=h/2; //starting particles from the centre at x=0
}

function setup() {
  createCanvas(w, h);  //canvas setup
  background(0);
  stroke(255);
  frameRate(60).smooth();
}

function draw() {
  if (x%5==0){ //small condition to update framerate dislay
    fill("black");
    stroke("black");
    rect(0,0,56,20);
    fill("white");
    stroke(0);
    text("FPS: "+floor(frameRate()),10,10);
  }
  x = (x + 1)%width; //x wrap around
  stroke(255);
  for (i = 0; i < n; i++) {
      point(x,xo[i]);
      xo[i]=xo[i]+random(-sigma,sigma); //random walk
  }
  if (x==width-1){
    fill("black");
    stroke("black");
    rect(5, height-amp/3,w/3,amp/3);//reset histo from previous update

    for (j = 0; j < n; j++) {
      for (i = 0; i < bars; i++) {
        if ((xo[j]>=i*height/bars) && (xo[j]<(i+1)*height/bars)){
          histogram[i]=histogram[i]+1; //increment previous histo with new data
        }
      }
    }
    for (i = 0; i < n; i++) {
        xo[i]=h/2; //reset initial position to start next lap
    }

  }

  var histosum=Sum(histogram); //to normalise histo
  for (i = 0; i < bars; i++) {
      fill("blue");
      stroke("white");
      rect(1+(w/(3*bars) +1)*i, height-amp*histogram[i]/(histosum), w/(3*bars), amp*histogram[i]/histosum);
  } //draw histo


}
function Sum(A) { //function for easy array summation
  var sum=0;
  for (i = 0; i < A.length; i++) {
      sum=sum+A[i];
  }
  return sum;
}
