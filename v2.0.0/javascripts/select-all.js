document.addEventListener("DOMContentLoaded", function() {
    const inlineCodes = document.querySelectorAll('.md-typeset code:not(pre code)');
    
    inlineCodes.forEach(el => {
        el.style.cursor = "pointer"; // show a pointer cursor
        el.addEventListener('click', function() {
            const range = document.createRange();
            range.selectNodeContents(this);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        });
    });
});