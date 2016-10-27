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

  var s_assembly = s.day() + '/' + s.month() + '/' + s.year();
  var f_assembly = f.day() + '/' + f.month() + '/' + f.year();

  window.open("http://localhost:5000/table?initial="+s_assembly+"&final="+f_assembly);
}
