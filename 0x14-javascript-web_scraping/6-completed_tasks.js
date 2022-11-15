#!/usr/bin/node
const request = require("request");

function getTotos() {
  const url = "https://jsonplaceholder.typicode.com/todos";

  request.get({ url }, (err, response, body) => {
    let results = JSON.parse(body);

    const user_tasks = {};
    for (let i = 1; i <= 10; i++) {
      const completed = results.filter(
        (t) => t.userId == i && t.completed == true
      );
      user_tasks[i] = completed.length;
    }

    console.log(user_tasks);
  });
}

getTotos();
