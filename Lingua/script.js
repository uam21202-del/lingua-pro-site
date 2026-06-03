// ===== БУРГЕР-МЕНЮ =====
document.addEventListener('DOMContentLoaded', function () {
  const burger = document.getElementById('burger');
  const navMenu = document.getElementById('navMenu');

  burger.addEventListener('click', function () {
    navMenu.classList.toggle('active');
    burger.classList.toggle('active');
  });

  // Закрыть меню при клике на ссылку
  navMenu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      navMenu.classList.remove('active');
      burger.classList.remove('active');
    });
  });

  // ===== СЛАЙДЕР ОТЗЫВОВ =====
  var slides = document.querySelectorAll('.slide');
  var dots = document.querySelectorAll('.dot');
  var currentIndex = 0;
  var slideInterval;

  // Показывает слайд по индексу
  function showSlide(index) {
    slides.forEach(function (slide) {
      slide.classList.remove('active');
    });
    dots.forEach(function (dot) {
      dot.classList.remove('active');
    });
    slides[index].classList.add('active');
    dots[index].classList.add('active');
    currentIndex = index;
  }

  // Переключение на следующий слайд (автопрокрутка)
  function nextSlide() {
    var next = (currentIndex + 1) % slides.length;
    showSlide(next);
  }

  // Клик по точкам навигации
  dots.forEach(function (dot) {
    dot.addEventListener('click', function () {
      var index = parseInt(this.getAttribute('data-index'));
      showSlide(index);
      resetTimer();
    });
  });

  // Сброс таймера при ручном переключении
  function resetTimer() {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, 5000);
  }

  // Запуск автопрокрутки (5 секунд)
  if (slides.length > 1) {
    slideInterval = setInterval(nextSlide, 5000);
  }

  // ===== ВАЛИДАЦИЯ ФОРМЫ =====
  var form = document.getElementById('leadForm');

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var name = form.querySelector('input[name="name"]').value.trim();
    var phone = form.querySelector('input[name="phone"]').value.trim();
    var language = form.querySelector('select[name="language"]').value;

    if (!name) {
      alert('Пожалуйста, введите ваше имя.');
      return;
    }
    if (!phone || phone.length < 10) {
      alert('Пожалуйста, введите корректный номер телефона.');
      return;
    }
    if (!language) {
      alert('Пожалуйста, выберите язык.');
      return;
    }

    // Имитация отправки
    var btn = form.querySelector('.btn');
    btn.textContent = 'Отправляем...';
    btn.disabled = true;

    setTimeout(function () {
      alert('Спасибо, ' + name + '! Мы свяжемся с вами в ближайшее время для бесплатного урока.');
      form.reset();
      btn.textContent = 'Отправить';
      btn.disabled = false;
    }, 1000);
  });
});
