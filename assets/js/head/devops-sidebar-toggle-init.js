(function () {
  try {
    if (window.localStorage.getItem("devops-sidebar-hidden") === "true") {
      document.documentElement.classList.add("hide-sidebar");
    }
  } catch (e) {
    /* localStorage unavailable (privacy mode, etc.) — default to visible sidebar */
  }
})();
