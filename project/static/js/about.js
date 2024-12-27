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