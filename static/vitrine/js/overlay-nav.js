$(document).ready(function(){
  $(".hamburger").click(function(){
      $(".overlay").fadeToggle(200);
     $(this).toggleClass('btn-open').toggleClass('btn-close');
  });
});
$('.overlay').on('click', function(){
  $(".overlay").fadeToggle(200);
  $("#hamburger").css({background-color: "$main-color",})
  $(".hamburger").toggleClass('btn-open').toggleClass('btn-close');
  open = false;
});

$(document).ready(function(){
$(".hamburger").click(function(){
  $(this).toggleClass("is-active");
});
});

