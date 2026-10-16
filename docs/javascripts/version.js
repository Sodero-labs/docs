document.addEventListener("DOMContentLoaded", function () {
  const fetchUrl = "/versions.json"; 

  fetch(fetchUrl)
    .then(res => {
      if (!res.ok) {
        return fetch("versions.json"); 
      }
      return res;
    })
    .then(res => {
      if (!res.ok) throw new Error("versions.json not found");
      return res.json();
    })
    .then(data => {
      const select = document.querySelector(".version-select");
      if (!select) return; 

      const pathSegments = window.location.pathname.split("/").filter(s => s !== "");
      const currentVersion = pathSegments[0];

      data.forEach(v => {
        const opt = document.createElement("option");
        opt.value = `/${v.version}/`;
        opt.text = v.title || v.version;

        if (v.version === currentVersion) {
          opt.selected = true;
        }
        select.appendChild(opt);
      });

      select.addEventListener("change", e => {
        window.location.href = e.target.value;
      });
    })
    .catch(err => {
      console.error("Version list could not be loaded:", err);
    });
});