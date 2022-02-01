(function($) {
    'use strict';

    $('.html').rProgressbar({
        percentage: 80,
        fillBackgroundColor: '#efea2e'
    });
    $('.css').rProgressbar({
        percentage: 90,
        fillBackgroundColor: '#efea2e'
    });

    $('.php').rProgressbar({
        percentage: 75,
        fillBackgroundColor: '#efea2e'
    });
    $('.java').rProgressbar({
        percentage: 75,
        fillBackgroundColor: '#efea2e'
    });

    $(".progress-i").each(function() {

        var $bar = $(this).find(".bar");
        var $val = $(this).find("span");
        var perc = parseInt($val.text(), 10);

        $({ p: 0 }).animate({ p: perc }, {
            duration: 3000,
            easing: "swing",
            step: function(p) {
                $bar.css({
                    transform: "rotate(" + (45 + (p * 1.8)) + "deg)", // 100%=180° so: ° = % * 1.8
                    // 45 is to add the needed rotation to have the green borders at the bottom
                });
                $val.text(p | 0);
            }
        });
    });

})(jQuery);