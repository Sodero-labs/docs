(function() {
  const STORAGE_KEY = "md_nav_expanded_ids";

  function saveNavState() {
    const expanded = Array.from(document.querySelectorAll(".md-nav__toggle:checked"))
      .map(el => el.id)
      .filter(id => id.length > 0);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(expanded));
  }

  function applyNavState() {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    
    saved.forEach(id => {
      if (!id) return;
      const checkbox = document.getElementById(id);
      if (checkbox) {
        checkbox.checked = true;
       
        const parentItem = checkbox.closest('.md-nav__item');
        if (parentItem) parentItem.setAttribute('data-keep-open', 'true');
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyNavState);
  } else {
    applyNavState();
  }

  document.addEventListener("change", (e) => {
    if (e.target && e.target.classList.contains("md-nav__toggle")) {
      const parentItem = e.target.closest('.md-nav__item');
      if (e.target.checked) {
        parentItem.setAttribute('data-keep-open', 'true');
      } else {
        parentItem.removeAttribute('data-keep-open');
      }
      saveNavState();
    }
  });

  if (typeof subscribe$ !== "undefined") {
    subscribe$.subscribe(() => {
      setTimeout(applyNavState, 100); 
    });
  }
})();