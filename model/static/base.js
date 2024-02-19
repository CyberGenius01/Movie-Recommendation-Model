const filterbtn = document.querySelector('.nav-view');
const navDropBox = document.querySelector('.nav-drop');

let j = 0;
filterbtn.addEventListener('click', () => {
    if (j % 2 == 0) {
        navDropBox.style.display = 'block';
        j++;
    } else {
        navDropBox.style.display = 'none';
        j++;
    }
    console.log(navDropBox.style.display)
})

const hearts = document.querySelectorAll('.heart-svg');
hearts.forEach(heart => {
    let heartVar = 0;
    heart.addEventListener('click', () => {
        if (heartVar == 0) {
            heart.firstElementChild.style.fill = 'rgb(235, 0, 65, 1)';
            heartVar = 1;
        } else {
            heart.firstElementChild.style.fill = 'rgba(0, 0, 0, 0.5)';
            heartVar = 0;
        }
    })
})

document.addEventListener('load', () => {
    let html = document.querySelector("html");
    let cleanHTML = html.innerHTML.replace("&#xFEFF; ", '');
    html.innerHTML = cleanHTML;

})

