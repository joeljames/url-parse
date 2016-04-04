function RegisterTableClickEvent() {
  $("#summaryTable").on("click", "td", function() {
    var value = $.trim($(this).text());
    var sourceDataElement = document.getElementById("sourceData");
    var sourceDataContent = document.getElementById("sourceData").innerHTML;
    sourceDataElement.innerHTML =  sourceDataContent.replace(
      RegExp("&lt;\/?(" + value + ")", "g"),
      "&lt;<strong><mark>$1</mark></strong>"
    );
  });
}

$(document).ready(function(){
  RegisterTableClickEvent();
});
