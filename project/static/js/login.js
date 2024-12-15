document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");

    loginForm.addEventListener("submit", function (event) {
        const formData = new FormData(loginForm);
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

        fetch(loginForm.action, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
            },
            body: formData,
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Login failed");
                }
                return response.text();
            })
            .then(data => {
                // Redirect to home page or display success message
                window.location.href = "/";
            })
            .catch(error => {
                // Handle errors (e.g., invalid username/password)
                const messagesDiv = document.getElementById("messages");
                messagesDiv.innerHTML = `<p class="error">${error.message}</p>`;
            });

        event.preventDefault(); // Prevent default form submission
    });
});