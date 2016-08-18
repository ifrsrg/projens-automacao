function doIT() {
  var init = new Date (document.getElementById('start').value);
  var end = new Date (document.getElementById('finish').value);

  var oi = init.getDate() + 1;
  console.log(oi);
}
