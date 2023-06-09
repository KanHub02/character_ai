export function generateHTML(results) {
    let html = '';
  
    results.forEach(obj => {
      html += `
        <div class="character">
          <img src="${obj.image}" class="character-image">
          <p class="character-title">${obj.title}</p>
          <p class="character-description">${obj.short_description}</p>
        </div>
      `;
    });
  
    return html;
  }