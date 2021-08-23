$(document).ready(function(){
  var $terms = [

'트렌치코트',
'코트',
'패딩',
'밀리터리',
'블레이저',
'레더재킷',
'퍼',
'반팔티셔츠',
'긴팔티셔츠',
'셔츠',
'블라우스',
'니트',
'후드',
'맨투맨',
'데님팬츠',
'미니스커트',
'스커트',
'슬랙스',
'숏팬츠',
'트레이닝',
'레깅스',
'운동화,'
'샌들',
'힐',
'로퍼',
'워커',
'원피스',
'백팩',
'토트백',
'클러치',
'숄더백',
'에코백',
     ].sort(),
     $return = [];
  function strInArray(str, strArray) {
    for (var j=0; j<strArray.length; j++) {
      if (strArray[j].match(str) && $return.length < 5) {
        var $h = strArray[j].replace(str, '<strong>'+str+'</strong>');
        $return.push('<li class="prediction-item"><span class="prediction-text">' + $h + '</span></li>');
      }
    }
  }

  function nextItem(kp) {
    if ( $('.focus').length > 0 ) {
      var $next = $('.focus').next(),
          $prev = $('.focus').prev();
    }

    if ( kp == 38 ) { // Up

      if ( $('.focus').is(':first-child') ) {
        $prev = $('.prediction-item:last-child');
      }

      $('.prediction-item').removeClass('focus');
      $prev.addClass('focus');

    } else if ( kp == 40 ) { // Down

      if ( $('.focus').is(':last-child') ) {
        $next = $('.prediction-item:first-child');
      }

      $('.prediction-item').removeClass('focus');
      $next.addClass('focus');
    }
  }

  $(function(){
    $('#kw').keydown(function(e){
      $key = e.keyCode;
      if ( $key == 38 || $key == 40 ) {
        nextItem($key);
        return;
      }

      setTimeout(function() {
        var $search = $('#kw').val();
        $return = [];

        strInArray($search, $terms);

        if ( $search == '' || ! $('input').val ) {
          $('.output').html('').slideUp();
        } else {
          $('.output').html($return).slideDown();
        }

        $('.prediction-item').on('click', function(){
          $text = $(this).find('span').text();
          $('.output').slideUp(function(){
            $(this).html('');
          });
          $('#kw').val($text);
        });

        $('.prediction-item:first-child').addClass('focus');

      }, 50);
    });
  });

    $('#kw').focus(function(){
      if ( $('.prediction-item').length > 0 ) {
        $('.output').slideDown();
      }

      $('#searchform').submit(function(e){
        e.preventDefault();
        $text = $('.focus').find('span').text();
        $('.output').slideUp();
        $('#kw').val($text);
        $('input').blur();
      });
    });

    $('#kw').blur(function(){
      if ( $('.prediction-item').length > 0 ) {
        $('.output').slideUp();
      }
    });

  });