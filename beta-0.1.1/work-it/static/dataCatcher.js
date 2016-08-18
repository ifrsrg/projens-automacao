(function() {
    var tbody = document.querySelector('tbody');
    console.log(tbody);

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

    readTextFile("/static/dumbster.json", function(text) {
        var data = JSON.parse(text);

        for (var i = 0; i < data.length; i++) {
            var tr = document.createElement('tr');

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].date;

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].umid;

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].temp;

            tbody.appendChild(tr);
        }

    });
}());
