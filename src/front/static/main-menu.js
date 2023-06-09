fetch('http://127.0.0.1:8080/api/v1/character-list/')
  .then(response => response.json())
  .then(data => {
    let html = '';

    data.results.forEach(obj => {
        html += `
          <div>
            <img src="${obj.image}">
            <p>${obj.title}</p>
            <p>${obj.short_description}</p>
          </div>
        `;
    });

    document.getElementById("data-content").innerHTML = html;

  })
  .catch(error => {
    console.log('Ошибка:', error);
  });