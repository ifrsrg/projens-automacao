/*
  Estudar tabelísticas por:
  https://github.com/tableless/exemplos/tree/gh-pages/melhorando-exibicao-tabelas-jquery

  Assim, realizar os casos de testes finais.
*/

metadata = []

function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

readTextFile("http://localhost:8000/dumbster.json", function(text){
    var data = JSON.parse(text);
    metadata = data;
    console.log(metadata);
});