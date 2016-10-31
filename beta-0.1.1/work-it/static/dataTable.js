function doIT() {
  var init = document.getElementById('start').value.split('/');
  var end = document.getElementById('finish').value.split('/');

  init = init[0] + '-' + init[1] + '-' + init[2];
  end = end[0] + '-' + end[1] + '-' + end[2];

  window.open("http://localhost:5000/table?initial="+init+"&final="+end);
}
