$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, _) {
  $.each(data.results, function (_, elmnt) {
    $('#list_movies').append(elmnt.title + '</br>');
  });
});
