var items = [
  { 'src': "./image/fukaseSekaowa.jpg", "ref": "http://r-humors.com/wp-content/uploads/2015/03/fuka.jpg" },
  { 'src': "./image/yamaguchiSakanakusyon.jpg", 'ref': "http://xn--vekw70ybyi.com/wp-content/uploads/yamaguchi.jpg" },
  { 'src': "./image/koizumiKanabun.jpg", 'ref': "http://natalie.mu/images/music/ja/sp-hear_walkman02/vBTaiwGH/ph04-1.jpg" },
  { 'src': "./image/meshidaKanabun.jpg", 'ref': "http://topic-intro.net/wp-content/uploads/2017/02/meshida-yuuma.jpg" },
  { 'src': "./image/kogaKanabun.jpg", 'ref': "http://natalie.mu/images/music/ja/sp-hear_walkman02/vBTaiwGH/ph02-1.jpg" },
  { 'src': "./image/taniguchiKanabun.jpg", 'ref': "http://s-bellkochan.com/wp-content/uploads/2015/05/photo06.jpg" },
  { 'src': "./image/kawataniGesukiwa.jpg", 'ref': "http://cdn.buzz-plus.com/wp-content/uploads/2016/01/kawatani01.jpg" },
  { 'src': "./image/nishinoKorochiki.jpg", 'ref': "http://monchanchi.montaro.xyz/wp-content/uploads/2017/01/d9f3593af86a8bd821e9a8da2c1ac760.jpg" },
  { 'src': "./image/inoueNonsuta.jpg", 'ref': "https://rr.img.naver.jp/mig?src=http%3A%2F%2Fimgcc.naver.jp%2Fkaze%2Fmission%2FUSER%2F20140908%2F23%2F2776033%2F17%2F385x480x74146eecf461e6edaf688fea.jpg%2F300%2F600&twidth=300&theight=600&qlt=80&res_format=jpg&op=r" },
  { 'src': "./image/yatsuiErekicomic.gif", 'ref': "http://news-diary1.com/wp-content/uploads/2013/11/2013-11-17_075500.gif" },
  { 'src': "./image/matayoshiPisu.jpg", 'ref': "https://wordleaf.c.yimg.jp/wordleaf/thepage/images/20150208-00000003-wordleaf/20150208-00000003-wordleaf-0d81b7c58d89b26cf9fa4de19e8cb4fb0.jpg" },
  { 'src': "./image/oshirikajirimushi.jpg", 'ref': "http://kinemacitrus.biz/blog/old_image//images/kajirimushi.jpg" },
  { 'src': "./image/katagiriRamens.jpg", 'ref': "http://doorto.net/wp-content/uploads/2016/05/katagirijin053101.jpg" },
  { 'src': "./image/nakaokaRochi.jpg", 'ref': "http://k-bass.com/wp-content/uploads/2015/09/%E3%83%AD%E3%83%83%E3%83%81%E3%80%80%E4%B8%AD%E5%B2%A1.jpg" }
]

var CARD_NUM = 8,
  FLIP_COUNT = 6,
  flipCount = FLIP_COUNT,
  $first = undefined,
  firstNum = undefined,
  secondNum = undefined,
  correctNum = 0,
  flipFlag = true;

$(function() { //called after finish to read html
  $('.js-reset').on('click', jsResetClicked);
  $('#js-contents').on('click', 'div', jsTileClicked);
  $('.js-expose').on('click', jsExposeClicked);
  $('.js-conceal').on('click', jsConcealClicked);
  initialize();
});

function jsResetClicked(e) {
  // console.log('reset clicked!');
  var valText = $('#number-text').val(); 
  // $('#number-text').val('8'); 
  var val = Number(valText) || 8;
  // console.log(val);
  if(val % 2 == 0 && val <= items.length * 2){
    CARD_NUM = val;
    FLIP_COUNT = Math.floor(val * 3 / 4);
  }
  // console.log(CARD_NUM);

  initialize();

  return e.preventDefault();
}

function jsTileClicked() {
  // console.log('Tile clicked! id:' + $(this).data('num') + " " + $(this).data('state'));
  // console.log($(this).children('span').html());
  flipCard($(this));
}

function jsExposeClicked(e){
  $(".Tile").removeClass("covered").addClass("uncovered");
  return e.preventDefault();
}

function jsConcealClicked(e){
  $(".Tile").removeClass("uncovered").addClass("covered");
  return e.preventDefault();
}

function initialize() {
  flipCount = FLIP_COUNT;
  $(".js-count").text(flipCount);
  $('#js-contents').html("");
  flipFlag = true;
  correctNum = 0;

  // console.log(CARD_NUM);


  //associate info with panel 
  //prepare random id array
  var randIds = [];
  for (var i = 0; i < CARD_NUM/2; i++) {
    items[i].id = i;
    randIds.push(i);
    randIds.push(i);
  }

  shuffle(randIds);

  for (var i = 0; i < randIds.length; i++) {
    for (var j = 0; j < items.length; j++) {
      if (randIds[i] == items[j].id) {
        addTile(items[j].src, items[j].ref, items[j].id);
      }
    }
  }
}

function addTile(imgsrc, imgref, tilenumber) {
  var tileStr = '<div class="Tile covered" data-num="' +
    tilenumber + '">' +
    '<span class="TileContents">' +
    '<img src=' + imgsrc + ' ref=' + imgref + " />" +
    '</span>' +
    '<span class="TileTiltle">' +
    '</span>' +
    '</div>';
  $('#js-contents').append(tileStr);
}

// <div class="Tile">
//     <span class="TileContents">
//       <img src="./image/fukaseSekaowa.jpg" ref="http://r-humors.com/wp-content/uploads/2015/03/fuka.jpg" />
//     </span>
//     <span class="TileTitle">
//     </span>
//   </div>

function flipCard($this) {
  // console.log('called flipCard');
  // console.log($this.data('state'));
  if (!flipFlag || !$this.hasClass("covered")) {
    return false;
  }

  var flipNum = $this.data("num");

  // console.log(flipNum);

  $this.removeClass("covered").addClass("uncovered");

  if (firstNum == undefined) {
    firstNum = flipNum;
    $first = $this;
  } else {
    secondNum = flipNum;
    $second = $this;
    flipFlag = false;

    // console.log('judge');
    if (firstNum == secondNum) {
      // console.log('o');
      correctNum++;
      flipFlag = true;

      if (correctNum == CARD_NUM / 2) {
        alert("Clear!!");
      }
    } else {
      // console.log('x');
      flipCount--;
      // console.log(flipCount);

      setTimeout(function() {
        $(".js-count").text(flipCount);
        $first.removeClass("uncovered").addClass("covered");
        $second.removeClass("uncovered").addClass("covered");

        if (flipCount == 0) {
          alert("Game Over");
        } else {
          flipFlag = true;
        }
      }, 500);
    }

    firstNum = undefined;
    secondNum = undefined;
  }
}

//https://bost.ocks.org/mike/shuffle/
function shuffle(array) {
  var n = array.length,
    t, i;

  while (n) {
    i = Math.floor(Math.random() * n--);
    t = array[n];
    array[n] = array[i];
    array[i] = t;
  }

  return array;
}