function feedback(spinner) {

    var panel = $('.feedback-content');
    var raw_form = ''

    var feedback = function (e) {
        panel.html(raw_form);

        bind_feedback();
    }

    var bind_feedback = function () {
        $('.feedback-form').submit(function (e) {
            var form = $(this);
            e.preventDefault();

            $.ajax({
                type: "POST",
                url: form.attr('action'),
                data: form.serialize(),
                beforeSend: function () {
                    $('form', panel).html("<p>Your nice message is sending to us.</p>");
                    $('form', panel).append(spinner);
                },
                error: function (data) {
                    $('form', panel).html('<p>Oh, something went wrong :(<br/><span class="glyphicon glyphicon-thumbs-down"></span></p>');
                    $('form', panel).append('<p><button type="button" class="renew-feedback btn btn-primary">Try again!</button></p>');
                    $('.renew-feedback').on('click', feedback);
                },
                success: function (data) {
                    if (data != "true") {
                        panel.html(data);
                        bind_feedback();
                        return false;
                    }
                    $('form', panel).html('<p>Success! :)<br/><span class="glyphicon glyphicon-thumbs-up"></span></p>');
                    $('form', panel).append('<p><button type="button" class="renew-feedback btn btn-primary">Send a (nice) new feedback</button></p>');

                    $('.renew-feedback').on('click', feedback);
                }
            });
        });
    }

    $.get(panel.attr('data-url'), function (data) {
        raw_form = data;
        panel.html(data);

        bind_feedback();
    });

    $('.expand-feedback').on('click', function (e) {
        e.preventDefault();

        if (panel.hasClass('no-expand')) {
            panel.addClass('expand').removeClass('no-expand');
            $(this).addClass('expand');
        } else {
            panel.addClass('no-expand').removeClass('expand');
            $(this).removeClass('expand');
        }
    })
}