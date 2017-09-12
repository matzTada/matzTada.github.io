var MAX_NUM;
var currentNum;
var drawItr;
var tmpItr;
var nums;

function setup() {
  createCanvas(1200, 800); // initialize canvas for drawing
  MAX_NUM = 100;
  nums = [];
  nums.push("dead"); //prepare "box" used as sieve
  for (var i = 1; i <= MAX_NUM; i++) {
    nums.push("alive"); // "alive" : alive, "dead" : dead(sieved)
  }
  nums[1] = "dead";
  currentNum = 1;
  // console.log(nums);
  drawStart();
  drawCurrent();
}

function draw() {
}

function keyTyped() {
  switch (key) {
    case ' ':
      currentNum += 1;
      if(currentNum > MAX_NUM){
        var x = 0;
        var y = height*9/10;
        fill(0);
        textSize(height/10)
        text("finish", x, y);
      }
      if (nums[currentNum] === "alive") {
        tmpItr = currentNum * 2;
        while(tmpItr <= MAX_NUM){
          tmpItr += currentNum;
          nums[tmpItr] = "dead";
        }
      }
      // console.log(nums);
      drawUpdate();
      drawCurrent();
      break;
  }
  return false;
}

function drawStart(){
  background(250);
  var x = 0;
  var y = 0;
  var rectSize = width / 20;
  drawItr = 1;
  while(drawItr <= MAX_NUM){
    fill(255, 255, 0);
    rect(x, y, rectSize, rectSize);
    fill(0);
    textSize(rectSize * 0.2);
    text(drawItr, x, y + rectSize);
    x += rectSize;
    if(floor(drawItr % 10) == 0){
      x = 0;
      y += rectSize;
    }
    drawItr += 1;
  }
}

function drawUpdate(){
  var x = 0;
  var y = 0;
  var rectSize = width / 20;
  drawItr = 1;
  while(drawItr <= MAX_NUM){
    if(floor(drawItr % currentNum == 0) && drawItr > currentNum){
      fill(0, 255 ,255);
      rect(x, y, rectSize, rectSize);
      fill(0);
      textSize(rectSize * 0.2);
      text(drawItr, x, y + rectSize);      
    }
    x += rectSize;
    if(floor(drawItr % 10) == 0){
      x = 0;
      y += rectSize;
    }
    drawItr += 1;
  }
}

function drawCurrent(){
  var x = 0;
  var y = 0;
  var rectSize = width / 20;
  drawItr = 1;
  while(drawItr <= currentNum-1){
    x += rectSize;
    if(floor(drawItr % 10) == 0){
      x = 0;
      y += rectSize;
    }
    drawItr += 1;
  }
  rectSize = width / 20 / 4;
  fill(0, 255, 0);
  rect(x, y, rectSize, rectSize);
  fill(0);
  textSize(rectSize * 0.2);
  text(drawItr, x, y + rectSize);
}
