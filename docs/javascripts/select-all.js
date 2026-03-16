document.addEventListener("DOMContentLoaded", function() {
    const inlineCodes = document.querySelectorAll('.md-typeset code:not(pre code)');
    
    inlineCodes.forEach(el => {
        el.style.cursor = "pointer"; // 마우스 커서를 포인터로
        el.addEventListener('click', function() {
            const range = document.createRange();
            range.selectNodeContents(this);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
        });
    });
});