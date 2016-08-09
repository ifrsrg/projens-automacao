function printDate() {
  for (var i = 0; i < metadata.length; i++) {
    document.writeln(metadata[i].date + "<br>");
  }
}

function printTemp() {
  for (var i = 0; i < metadata.length; i++) {
    document.writeln(metadata[i].temp + "<br>");
  }
}

function printUmid() {
  for (var i = 0; i < metadata.length; i++) {
    document.writeln(metadata[i].umid + "<br>");
  }
}
