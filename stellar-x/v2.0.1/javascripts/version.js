// Product and version menus in the header.
// Pages live at /<product>/<version>/..., for example /stellar-x/v2.0.0/station/overview/,
// and each product folder has its own versions.json written by mike.
(function () {
  var segments = window.location.pathname.split("/").filter(function (s) { return s !== ""; });
  var product = segments[0];
  var current = segments[1];

  function addVersions(select, versions) {
    versions.forEach(function (v) {
      var opt = document.createElement("option");
      opt.value = "/" + product + "/" + v.version + "/";
      opt.text = v.title || v.version;
      if (v.version === current || (v.aliases || []).indexOf(current) !== -1) {
        opt.selected = true;
      }
      select.appendChild(opt);
    });
    select.addEventListener("change", function (e) {
      window.location.href = e.target.value;
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".product-select").forEach(function (select) {
      select.addEventListener("change", function (e) {
        window.location.href = "/" + e.target.value + "/";
      });
    });

    var selects = document.querySelectorAll(".version-select");
    if (!selects.length || !product) return;

    fetch("/" + product + "/versions.json")
      .then(function (res) {
        if (!res.ok) throw new Error("versions.json not found");
        return res.json();
      })
      .then(function (versions) {
        selects.forEach(function (select) { addVersions(select, versions); });
      })
      .catch(function () {
        // Local previews have no versions.json: hide the empty menu.
        selects.forEach(function (select) {
          var box = select.closest(".version-dropdown");
          if (box) box.hidden = true;
        });
      });
  });
})();
