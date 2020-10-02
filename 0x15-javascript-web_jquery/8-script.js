$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  $.each(data.results, (index) => {
    $('#list_movies').append('<li>' + data.results[index].title + '</li>');
  });
});
