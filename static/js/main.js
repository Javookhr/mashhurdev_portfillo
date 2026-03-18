/**
 * Safobek Portfolio – main.js
 * Tab tizimi va scroll behaviori
 */

document.addEventListener('DOMContentLoaded', () => {

  // --- Tab tizimi ---
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabSections = document.querySelectorAll('.tab-section');
  const cardBody = document.getElementById('cardBody');
  const stickyHeader = document.getElementById('stickyHeader');

  function switchTab(tabName) {
    // Barcha sectionlarni yashir
    tabSections.forEach(sec => sec.classList.remove('active'));
    tabBtns.forEach(btn => btn.classList.remove('active'));

    // Tanlangan tabni ko'rsat
    const target = document.getElementById(`section-${tabName}`);
    if (target) {
      target.classList.add('active');
    }

    // Tugmani belgilab qo'y
    const activeBtn = document.querySelector(`.tab-btn[data-tab="${tabName}"]`);
    if (activeBtn) {
      activeBtn.classList.add('active');
    }

    // Sahifani yuqoriga scroll qil
    if (cardBody) {
      cardBody.scrollTop = 0;
    }
  }

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.getAttribute('data-tab');
      switchTab(tab);
    });
  });

  // --- Sticky header: faqat haqida tabida scroll bo'lganda ko'rsin ---
  if (cardBody && stickyHeader) {
    cardBody.addEventListener('scroll', () => {
      const activeSection = document.querySelector('.tab-section.active');
      if (activeSection && activeSection.id === 'section-haqida') {
        if (cardBody.scrollTop > 60) {
          stickyHeader.classList.add('visible');
        } else {
          stickyHeader.classList.remove('visible');
        }
      } else {
        stickyHeader.classList.remove('visible');
      }
    });
  }

  // --- Timeline itemlarini animatsiya qilish (IntersectionObserver) ---
  const timelineItems = document.querySelectorAll('.timeline-item');
  if (timelineItems.length > 0) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateX(0)';
          }, i * 80);
        }
      });
    }, { threshold: 0.1 });

    timelineItems.forEach(item => {
      item.style.opacity = '0';
      item.style.transform = 'translateX(-15px)';
      item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
      observer.observe(item);
    });
  }

  // --- Social itemlarini hover ta'sirini kuchaytirish ---
  const socialItems = document.querySelectorAll('.social-item');
  socialItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.style.transition = 'all 0.2s ease';
    });
  });

  // URL hash orqali tabni ochish (masalan, safobek.uz/#aloqa)
  const hash = window.location.hash.replace('#', '');
  const validTabs = ['haqida', 'tajriba', 'tarmoqlar', 'aloqa'];
  if (hash && validTabs.includes(hash)) {
    switchTab(hash);
  }

});
