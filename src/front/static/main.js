fetch('http://127.0.0.1:8080/api/v1/character-list/')
  .then(response => response.json())
  .then(data => {
    let html = '';

    data.results.forEach(obj => {
        html += `
          <div class="character">
            <img src="${obj.image}" class="character-image">
            <p class="character-title">${obj.title}</p>
            <p class="character-description">${obj.short_description}</p>
          </div>
        `;
    });

    document.getElementById("data-content").innerHTML = html;

  })
  .catch(error => {
    console.log('Ошибка:', error);
  });