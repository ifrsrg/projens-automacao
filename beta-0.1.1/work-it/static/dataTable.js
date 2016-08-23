/* Apenas algumas lógicas fraquinhas para intervalo de tempo
   Serão melhoradas posterirormente! Ex: Objetos :) */

function doIT() {
  var init = new Date (document.getElementById('start').value);
  var end = new Date (document.getElementById('finish').value);
  console.log(init);

  var di = init.getDate();
  var df = end.getDate();

  if ((di == 31)||(df == 31)) {
    di = 1;
    df = 1;
  } else {
    di += 1;
    df += 1;
  }

  var mi = init.getMonth();
  console.log("dia inicial: " + di + ";");
  console.log("mes inicial: " + mi + ";");
}
