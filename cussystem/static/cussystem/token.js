function Token(){
    return $('[name="csrfmiddlewaretoken"]').val();
}

$.ajaxSetup({
      cache: false,
      beforeSend: function (xhr, settings) {
              xhr.setRequestHeader("X-CSRFToken", Token());
      }
  });