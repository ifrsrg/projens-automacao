/* Uma espécie de objeto foi implementado :) */

function Daten(string) {
  this.day = function() {return parseInt(string.substring(0, 2));}
  this.month = function() {return parseInt(string.substring(3, 5))};
  this.year = function() {return parseInt(string.substring(6, 10))};
}

function doIT() {
  var init = document.getElementById('start').value;
  var end = document.getElementById('finish').value;

  var s = new Daten(init);
  var f = new Daten(end);

  console.log(s.day());
  console.log(s.month());
  console.log(s.year());

  console.log();

  console.log(f.day());
  console.log(f.month());
  console.log(f.year());

  window.open("http://localhost:5000/table");

}
