document.addEventListener('DOMContentLoaded', () => {

    const bioForm = document.getElementById('bioForm');
    const previewContent = document.getElementById('previewContent');

    bioForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const photoUrl = document.getElementById('photoUrl').value;
        
        const link1Title = document.getElementById('link1Title').value;
        const link1Url = document.getElementById('link1Url').value;
        
        const link2Title = document.getElementById('link2Title').value;
        const link2Url = document.getElementById('link2Url').value;

        const previewHTML = `
            <img src="${photoUrl}" alt="Foto de ${name}" class="profile-pic">
            <h3 class="profile-name">@${name}</h3>
            
            <a href="${link1Url}" target="_blank" class="bio-link">${link1Title}</a>
            <a href="${link2Url}" target="_blank" class="bio-link">${link2Title}</a>
        `;

        previewContent.innerHTML = previewHTML;
    });
});