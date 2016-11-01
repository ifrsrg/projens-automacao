function doIT() {
  var init = document.getElementById('start').value.split('/');
  var end = document.getElementById('finish').value.split('/');

  init = init[2] + '-' + init[1] + '-' + init[0];
  end = end[2] + '-' + end[1] + '-' + end[0];

  window.open("http://localhost:5000/table?initial="+init+"&final="+end);
}
