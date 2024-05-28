document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star-rating label');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const rating = star.previousElementSibling.value;
            const input = document.querySelector(`input[value="${rating}"]`);
            input.checked = true;
        });

        star.addEventListener('mouseover', () => {
            stars.forEach(s => s.style.color = '#ddd');
            star.style.color = '#f5b301';
            let previous = star.previousElementSibling;
            while (previous && previous.tagName === 'LABEL') {
                previous.style.color = '#f5b301';
                previous = previous.previousElementSibling;
            }
        });

        star.addEventListener('mouseout', () => {
            stars.forEach(s => s.style.color = '#ddd');
            const checked = document.querySelector('.star-rating input[type="radio"]:checked');
            if (checked) {
                let checkLabel = checked.nextElementSibling;
                while (checkLabel) {
                    checkLabel.style.color = '#f5b301';
                    checkLabel = checkLabel.nextElementSibling;
                }
            }
        });
    });
});
