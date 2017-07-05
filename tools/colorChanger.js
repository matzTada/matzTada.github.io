// var colorArray = ["style1", "style2", "style3", "style4", "style5", "style6", "style7"]
// var colorArray = ["style1", "style2"]

function changeColor(colorArray) {
  var colorArrayItr = 0

  var arts = document.getElementsByTagName("article");
  for ( var i = 0; i < arts.length; i++){
      var tmpClassName = arts[i].getAttribute("class");
      // console.log(tmpClassName);
     
      if (tmpClassName != "style0"){
        arts[i].className = colorArray[colorArrayItr]     
        colorArrayItr += 1;
        if(colorArrayItr >= colorArray.length){
            colorArrayItr = 0;
        }
      }
      else{
        arts[i].className = "style0";         
      }
  }
};

// changeColor(["style1", "style5"]);