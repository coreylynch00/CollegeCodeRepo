var faq = document.getElementsByClassName("faq_page");
var i;
for (i = 0; i < faq.length; i++) {
    /* EVENT LISTENER TO DETERMINE WHICH FAQ IS CLICKED */
    faq[i].addEventListener("click", function () {
        /* SWITCH BETWEEN ACTIVE CLASS TO HIGHLIGHT FAQ WHEN IT IS CLICKED ON */
        this.classList.toggle("active");
        /* HIDE/SHOW THE FAQ THAT IS CLICKED ON */
        var body = this.nextElementSibling;
        if (body.style.display === "block") {
            body.style.display = "none";
        } else {
            body.style.display = "block";
        }
    });
}
