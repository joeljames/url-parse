function getRandHex() {
    return (Math.floor(Math.random() * 56) + 200).toString(16);
}

function getRandomColor() {
    var color = "#" + getRandHex() + getRandHex() + getRandHex();
    if($.inArray(color, usedColor) == -1) {
      usedColor.push(color);
      return color
    } else {
      getRandomColor();
    }
}

function RegisterTableClickEvent() {
  // Global used color list
  usedColor = new Array();
  $("#summaryTable").on("click", "td", function() {
    var value = $.trim($(this).text());
    var sourceDataElement = document.getElementById("sourceData");
    var sourceDataContent = document.getElementById("sourceData").innerHTML;
    var color = getRandomColor();
    sourceDataElement.innerHTML =  sourceDataContent.replace(
      RegExp("&lt;\/?(" + value + ")", "g"),
      '&lt;<strong><span style="background-color:' + color + '">$1</span></strong>'
    );
  });
}

$(document).ready(function(){
  RegisterTableClickEvent();
});
