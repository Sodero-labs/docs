document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.select-all').forEach(el => {
        el.style.cursor = "pointer"; 
        el.addEventListener('click', function() {
            const range = document.createRange();
            range.selectNodeContents(this);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        });
    });
});