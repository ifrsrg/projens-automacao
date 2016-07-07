/*
  Estudar tabelísticas por:
  https://github.com/tableless/exemplos/tree/gh-pages/melhorando-exibicao-tabelas-jquery

  Assim, realizar os casos de testes finais.
*/
metadata = [];

function readFile(callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", "dumbster.json", true);
  rawFile.onreadystatechange = function () {
    if ((rawFile.readyState === 4)&&(rawFile.status == "200")) callback(rawFile.responseText);
  }
  rawFile.send(null);
}

function init() {
  readFile(function(response) {
    var data = JSON.parse(response);
    metadata = data;
  });
  return metadata;
}

metadata = init();
