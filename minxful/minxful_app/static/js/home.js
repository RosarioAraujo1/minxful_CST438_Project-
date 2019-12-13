$(document).ready(function () {
    $('.modal').hide();
    $(".btn btn-default").click(function () {
        $('.modal').show();
    });

    $('.post p').css({ height: '35px', overflow: 'hidden' });
    $('.click').on('click', function () {
        // var id = $(this).attr('class');
        var $this = $(".post p");
        // var $this = $(id);
        if ($this.data('open')) {
            $this.animate({ height: '20px' });
            $this.data('open', 0);
            $('.click').html('Read More');

        }
        else {
            $this.animate({ height: '100%' });
            $this.data('open', 1);
            $('.click').html('Read Less');
        }
    });


});

