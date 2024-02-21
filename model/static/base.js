const filterbtn = document.querySelector('.nav-view');
const navDropBox = document.querySelector('.nav-drop');
let j = 0;
/*filterbtn.addEventListener('click', () => {
    if (j % 2 == 0) {
        navDropBox.style.display = 'block';
        j++;
    } else {
        navDropBox.style.display = 'none';
        j++;
    }
});
*/
console.log(j);
document.addEventListener('click', (e) => {
    if (j % 2 == 0) {
        if ((e.target === navDropBox ||
            e.target.parentElement.parentElement === navDropBox ||
            e.target.parentElement.parentElement.parentElement === navDropBox ||
            e.target.parentElement.parentElement.parentElement.parentElement === navDropBox) &&
            (e.target === filterbtn ||
                e.target.parentElement === filterbtn ||
                e.target.parentElement.parentElement === filterbtn)) {
            console.log(e.target);
            navDropBox.style.display = 'block';
        }
    } else {
        console.log(e.target);
        navDropBox.style.display = 'none';
        j++;
    }
});


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


