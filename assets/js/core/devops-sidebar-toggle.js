(function () {
  function setLabel(btn, hidden) {
    var label = hidden ? "Show sidebar" : "Hide sidebar";
    btn.setAttribute("aria-label", label);
    btn.setAttribute("title", label);
    btn.setAttribute("aria-pressed", hidden ? "true" : "false");
  }

  function init() {
    var btn = document.getElementById("devops-sidebar-toggle");
    if (!btn) return;

    setLabel(btn, document.documentElement.classList.contains("hide-sidebar"));

    btn.addEventListener("click", function () {
      var hidden = document.documentElement.classList.toggle("hide-sidebar");
      setLabel(btn, hidden);
      try {
        window.localStorage.setItem("devops-sidebar-hidden", hidden ? "true" : "false");
      } catch (e) {
        /* localStorage unavailable — toggle still works for this page view */
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
