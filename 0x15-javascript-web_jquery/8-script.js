$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
  const list = $("UL#list_movies");
  $.each(data.results, function (index, item) {
    const listItem = $("<li></li>").text(item.title);
    list.append(listItem);
  });
});
