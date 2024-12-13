function uiLoader() {
  let servicesContainer;
  if (document.querySelector(".standVideos") == null) {
    servicesContainer = null;
  } else {
    servicesContainer = document.querySelector(".standVideos");
  }

  if (servicesContainer == null) return;

  let services = [
    {
      title: "Interactive Courses",
      icon: "fa-solid fa-book",
      description: "Engage in hands-on learning experiences.",
    },
    {
      title: "Expert Tutors",
      icon: "fa-solid fa-chalkboard-user",
      description: "Learn from industry-leading experts.",
    },
    {
      title: "Community Support",
      icon: "fa-solid fa-people-group",
      description: "Collaborate and grow with peers worldwide.",
    },
    {
      title: "Certification",
      icon: "fa-solid fa-certificate",
      description: "Earn accredited certifications to advance your career.",
    },
  ];

  services.forEach(({ title, icon, description }) => {
    let servicesBox = `
   <div class="services-box">
    <div class="box-title">
    <i class="${icon}"></i>
    <h3>${title}</h3>
    </div>
    <p>${description}</p>

   </div>
   `;

    if (servicesContainer != null)
      servicesContainer.insertAdjacentHTML("beforeend", servicesBox);
  });
}

uiLoader();

window.onscroll = function () {
  myScrollFunction();
};

function myScrollFunction() {
  if (
    document.body.scrollTop > 100 ||
    document.documentElement.scrollTop > 100
  ) {
    document.getElementById("header").classList.add("animateHeader");
  } else {
    document.getElementById("header").classList.remove("animateHeader");
  }
}
