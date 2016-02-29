function loadVF(filename) {
    $.getJSON('data/' + filename + '.json', function(data) {
        data.forEach(function(item, i) {
            question = $('<div id="q' + i + '" data-answer="' + item.answer + '">').attr('class', 'well');
            question.append($('<p>').html(item.statement));
            question.append($('<input type="button" style="margin-right: 5px" class="btn btn-default" id="q' + i + '1" value="Vrai" onclick="verify(this.parentNode, \'true\');" />'));
            question.append($('<input type="button" class="btn btn-default" id="q' + i + '0" value="Faux" onclick="verify(this.parentNode, \'false\');" />'));
            $('#vf').append(question);
        });
    });
}

function verify(id, herAnswer) {
    answer = $(id).attr('data-answer');
    color = (answer == herAnswer) ? "success" : "danger";
    console.log(answer);
    $('#' + $(id).attr('id') + ((answer == 'true') ? 1 : 0)).addClass('btn-' + color);
}
