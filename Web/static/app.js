const filled = document.querySelector('.filled');

function update () {
  filled.style.width = `${(window.scrollY) / (document.body.scollHeight - window.innerHeight) * 100}%`
  requestAnimationFrame();
}

update();