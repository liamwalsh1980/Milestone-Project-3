function sendMail(contactForm) {
    // sets a new variable ready to use further down the code
    var modal = document.getElementById("modal");

    // Source of code from EmailJS using Email templates. This enables all successful feedback forms to be sent as an email
    emailjs.send("gmail", "filmzone", {
            "firstname": contactForm.firstname.value,
            "lastname": contactForm.lastname.value,
            "email": contactForm.email.value,
            "message": contactForm.message.value
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                // Bespoke message to the user specifically to the 'name' of the user within the Modal
                $(".modal-text-message").text("Thank you for your message " + contactForm.firstname.value + ". If you haven't already signed up to FilmZone, register for free today.");
                modal.style.display = "block";
                // reloads the form once the user clicks the close button in the Modal
                $("#closing-btn").click(function () {
                    location.reload();
                });
            },
            function (error) {
                console.log("FAILED", error);
                // Bespoke message to the user specifically to the 'name' of the user within the Modal
                $(".modal-text-message").text("Sorry " + contactForm.firstname.value + " something went wrong. Please try submitting your message again!");
                modal.style.display = "block";
                // reloads the form once the user clicks the close button in the Modal
                $("#closing-btn").click(function () {
                    location.reload();
                });
            });
    // Blocks the form from loading 
    return false;
}



