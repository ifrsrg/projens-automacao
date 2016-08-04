function printDate() {
  var printBox = []
  for (var i = 0; i < metadata.length; i++) printBox[i] = (metadata[i].date + "<br>");
  return printBox;
}

function printTemp() {
  var printBox = []
  for (var i = 0; i < metadata.length; i++) printBox[i] = (metadata[i].temp + "<br>");
  return printBox;
}

function printUmid() {
  var printBox = []
  for (var i = 0; i < metadata.length; i++) printBox[i] = (metadata[i].umid + "<br>");
  return printBox;
}
