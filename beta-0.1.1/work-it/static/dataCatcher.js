
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

        var aloha = window.location.href.split('/');
        var mahalo = aloha[3].split('?');
        var initial = mahalo[1].split('=')[1].split('&')[0];
        var final = mahalo[1].split('=')[2];

        console.log(initial + " // " + final);

        for (var i = 0; i < data.length; i++) {
            var tr = document.createElement('tr');

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].date;

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].temp;

            var td = document.createElement('td');
            tr.appendChild(td);
            td.innerText = data[i].umid;

            tbody.appendChild(tr);
        }



    });
}());
