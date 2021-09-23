$.ajax({
  type: "GET",
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (response) {
    for (const movie in response.results) {
      $('UL#list_movies').append("<li>" + response.results[movie].title + "</li>");
    }
  }
});
