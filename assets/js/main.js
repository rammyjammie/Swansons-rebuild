/* Swanson's Welding & Fabrication — site behavior
   Progressive enhancement only: every page works with JS disabled. */
(function () {
  "use strict";

  /* ---- Mobile navigation ------------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });

    // Close the panel on Escape, and when a link is chosen.
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
        toggle.focus();
      }
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      }
    });
  }

  /* ---- Header shadow once the page scrolls ------------------------------ */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- Reveal on scroll ------------------------------------------------ */
  /* Decorative only. Content must never stay hidden, so this resolves three
     ways: the observer fires, a safety timer sweeps up anything left, or the
     `.js` class is absent entirely and CSS never hides it in the first place. */
  var reveals = document.querySelectorAll(".reveal");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var revealAll = function () {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  };

  if (!reveals.length) {
    /* nothing to do */
  } else if (reduced || !("IntersectionObserver" in window)) {
    revealAll();
  } else {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.05 }
    );
    reveals.forEach(function (el) { io.observe(el); });

    // Safety net: if anything is still hidden a few seconds in, show it.
    window.setTimeout(revealAll, 4000);
    // And never let a print or tab-restore catch content mid-fade.
    window.addEventListener("beforeprint", revealAll);
  }

  /* ---- Current year in the footer --------------------------------------- */
  var year = document.querySelector("[data-year]");
  if (year) { year.textContent = new Date().getFullYear(); }
})();
