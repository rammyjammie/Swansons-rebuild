(($) => {
	$(window).ready(function () {
		// Initialize AOS library.
		setTimeout(function () {
			if (typeof AOS !== "undefined") {
				AOS.init({
					once: true,
				});
			}
		}, 100);
	});
})(jQuery);
