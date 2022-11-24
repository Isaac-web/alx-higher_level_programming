$("div#add_item").click(function () {
  const listItem = $("<li></li>").text("Item");
  $("UL.my_list").append(listItem);
});
