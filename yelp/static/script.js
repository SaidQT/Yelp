let nextBtn = document.querySelector('.next');
let prevBtn = document.querySelector('.prev');

let slider = document.querySelector('.slider');
let sliderList = slider.querySelector('.slider .list');
let thumbnail = document.querySelector('.slider .thumbnail');
let thumbnailItems = thumbnail.querySelectorAll('.item');

thumbnail.appendChild(thumbnailItems[0]);

// Function for next button 
nextBtn.onclick = function () {
     moveSlider('next');
}

// Function for prev button 
prevBtn.onclick = function () {
     moveSlider('prev');
}

function moveSlider(direction) {
     let sliderItems = sliderList.querySelectorAll('.item');
     let thumbnailItems = document.querySelectorAll('.thumbnail .item');

     if (direction === 'next') {
          sliderList.appendChild(sliderItems[0]);
          thumbnail.appendChild(thumbnailItems[0]);
          slider.classList.add('next');
     } else {
          sliderList.prepend(sliderItems[sliderItems.length - 1]);
          thumbnail.prepend(thumbnailItems[thumbnailItems.length - 1]);
          slider.classList.add('prev');
     }

     slider.addEventListener('animationend', function () {
          if (direction === 'next') {
               slider.classList.remove('next');
          } else {
               slider.classList.remove('prev');
          }
     }, { once: true }); // Remove the event listener after it's triggered once
}

// Autoplay functionality
let autoplayInterval = setInterval(() => {
     nextBtn.click();
}, 3000); // Change slide every 3 seconds

// Pause autoplay on mouse hover
slider.addEventListener('mouseover', () => {
     clearInterval(autoplayInterval);
});

// Resume autoplay when not hovering
slider.addEventListener('mouseout', () => {
     autoplayInterval = setInterval(() => {
          nextBtn.click();
     }, 4000);
});

window.addEventListener('scroll', function () {
     var header = document.querySelector('header');
     if (window.scrollY > 500) { 
          header.classList.add('scrolled');
     } else {
          header.classList.remove('scrolled');
     }
});
