fetch('http://127.0.0.1:8080/api/v1/character-list/')
  .then(response => response.json())
  .then(data => {
    let html_title = '';
    let html_image = '';
    let html_short_description = "";
    

    data.results.forEach(obj => {
        html_image += `<img src="${obj.image}">`;
        html_title += `<p>${obj.title}</p>`;
        html_short_description += `<p>${obj.short_description}</p>`
        document.getElementById("data-content").innerHTML = html_image, html_title, html_short_description;
    });

  })
  .catch(error => {
    console.log('Ошибка:', error);
  });