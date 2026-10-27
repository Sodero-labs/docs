(function() {
  if (window.__navState) return;
  window.__navState = true;

  // --- Sidebar toggle state persistence ---

  function restoreNavState() {
    var toggles = document.querySelectorAll(".md-nav__toggle");
    for (var i = 0; i < toggles.length; i++) {
      var toggle = toggles[i];
      if (!toggle.id) continue;
      var saved = sessionStorage.getItem("nav-" + toggle.id);
      if (saved === "1") toggle.checked = true;
      else if (saved === "0") toggle.checked = false;
    }
  }

  document.addEventListener("change", function(e) {
    var t = e.target;
    if (t.classList.contains("md-nav__toggle") && t.id) {
      sessionStorage.setItem("nav-" + t.id, t.checked ? "1" : "0");
    }
  });

  // --- Breadcrumb sync ---
  // #breadcrumb-source is inside the content block (replaced on instant nav)
  // Copy its contents to the header breadcrumbs

  function updateBreadcrumbs() {
    var source = document.getElementById("breadcrumb-source");
    var target = document.querySelector(".header-breadcrumbs");
    if (source && target) {
      target.innerHTML = source.innerHTML;
    }
  }

  // --- Hook into MkDocs Material page lifecycle ---

  if (typeof document$ !== "undefined") {
    document$.subscribe(function() {
      restoreNavState();
      updateBreadcrumbs();
    });
  } else {
    document.addEventListener("DOMContentLoaded", function() {
      restoreNavState();
      updateBreadcrumbs();
    });
  }
})();
