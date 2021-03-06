(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
function getRandHex() {
  // Returns a random hex code
  // Add a value 200 to make the hex code of light color
  return (Math.floor(Math.random() * 56) + 200).toString(16);
}

function getRandomColor() {
  // Return a color every time this method is called
  // Keeps a track of previously returned color so that
  // next time this method is called a new unique color is returned.
  var color = "#" + getRandHex() + getRandHex() + getRandHex();
  if($.inArray(color, usedColor) == -1) {
    usedColor.push(color);
    return color
  } else {
    getRandomColor();
  }
}

function RegisterTableClickEvent() {
  // usedColor arry keeps a track of previously used color.
  usedColor = new Array();
  $("#summaryTable").on("click", "td", function() {
    var value = $.trim($(this).text());
    var sourceDataElement = document.getElementById("sourceData");
    var sourceDataContent = document.getElementById("sourceData").innerHTML;
    var color = getRandomColor();
    // Regex to capture a tag
    var tagRegex = RegExp("&lt;\/?(" + value + ")", "g");
    sourceDataElement.innerHTML =  sourceDataContent.replace(
      tagRegex,
      '&lt;<strong><span style="background-color:' + color + '">$1</span></strong>'
    );
  });
}

$(document).ready(function(){
  RegisterTableClickEvent();
});

},{}]},{},[1]);
